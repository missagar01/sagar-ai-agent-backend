"""
Complete Database Schema Inspector
===================================
Extracts detailed metadata for checklist, delegation, and users tables
including columns, types, constraints, indexes, relationships, and sample data.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', '5432')
}

TABLES = ['checklist', 'delegation', 'users']

class DatabaseInspector:
    """Comprehensive database schema inspector"""
    
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Connect to database"""
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            print("✅ Database connected successfully")
            return True
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            return False
    
    def get_table_columns(self, table_name):
        """Get detailed column information"""
        query = """
        SELECT 
            c.column_name,
            c.data_type,
            c.character_maximum_length,
            c.numeric_precision,
            c.numeric_scale,
            c.is_nullable,
            c.column_default,
            pgd.description as column_comment
        FROM 
            information_schema.columns c
        LEFT JOIN 
            pg_catalog.pg_statio_all_tables st ON c.table_name = st.relname
        LEFT JOIN 
            pg_catalog.pg_description pgd ON pgd.objoid = st.relid 
            AND pgd.objsubid = c.ordinal_position
        WHERE 
            c.table_name = %s
            AND c.table_schema = 'public'
        ORDER BY 
            c.ordinal_position;
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_primary_keys(self, table_name):
        """Get primary key constraints"""
        query = """
        SELECT 
            kcu.column_name,
            tc.constraint_name
        FROM 
            information_schema.table_constraints tc
        JOIN 
            information_schema.key_column_usage kcu 
            ON tc.constraint_name = kcu.constraint_name
        WHERE 
            tc.table_name = %s
            AND tc.constraint_type = 'PRIMARY KEY'
            AND tc.table_schema = 'public';
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_foreign_keys(self, table_name):
        """Get foreign key relationships"""
        query = """
        SELECT
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name,
            tc.constraint_name
        FROM 
            information_schema.table_constraints AS tc 
        JOIN 
            information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
        JOIN 
            information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
        WHERE 
            tc.constraint_type = 'FOREIGN KEY' 
            AND tc.table_name = %s
            AND tc.table_schema = 'public';
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_indexes(self, table_name):
        """Get table indexes"""
        query = """
        SELECT
            indexname,
            indexdef
        FROM
            pg_indexes
        WHERE
            tablename = %s
            AND schemaname = 'public';
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_unique_constraints(self, table_name):
        """Get unique constraints"""
        query = """
        SELECT
            tc.constraint_name,
            kcu.column_name
        FROM
            information_schema.table_constraints tc
        JOIN
            information_schema.key_column_usage kcu 
            ON tc.constraint_name = kcu.constraint_name
        WHERE
            tc.table_name = %s
            AND tc.constraint_type = 'UNIQUE'
            AND tc.table_schema = 'public';
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_check_constraints(self, table_name):
        """Get check constraints"""
        query = """
        SELECT
            con.conname AS constraint_name,
            pg_get_constraintdef(con.oid) AS constraint_definition
        FROM
            pg_catalog.pg_constraint con
        JOIN
            pg_catalog.pg_class rel ON rel.oid = con.conrelid
        JOIN
            pg_catalog.pg_namespace nsp ON nsp.oid = connamespace
        WHERE
            rel.relname = %s
            AND con.contype = 'c'
            AND nsp.nspname = 'public';
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchall()
    
    def get_table_stats(self, table_name):
        """Get table statistics"""
        query = f"""
        SELECT 
            COUNT(*) as total_rows,
            pg_size_pretty(pg_total_relation_size(%s)) as total_size,
            pg_size_pretty(pg_relation_size(%s)) as table_size,
            pg_size_pretty(pg_indexes_size(%s)) as indexes_size
        FROM {table_name};
        """
        self.cursor.execute(query, (table_name, table_name, table_name))
        return self.cursor.fetchone()
    
    def get_sample_data(self, table_name, limit=5):
        """Get sample rows"""
        query = f"SELECT * FROM {table_name} LIMIT %s;"
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()
    
    def get_null_analysis(self, table_name):
        """Analyze NULL values in each column"""
        columns_info = self.get_table_columns(table_name)
        null_analysis = []
        
        for col in columns_info:
            col_name = col['column_name']
            query = f"""
            SELECT 
                COUNT(*) as total_rows,
                COUNT({col_name}) as non_null_count,
                COUNT(*) - COUNT({col_name}) as null_count,
                ROUND(100.0 * (COUNT(*) - COUNT({col_name})) / COUNT(*), 2) as null_percentage
            FROM {table_name};
            """
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            null_analysis.append({
                'column': col_name,
                **result
            })
        
        return null_analysis
    
    def get_distinct_values(self, table_name, column_name, limit=20):
        """Get distinct values for a column"""
        try:
            query = f"""
            SELECT 
                {column_name} as value,
                COUNT(*) as count
            FROM {table_name}
            WHERE {column_name} IS NOT NULL
            GROUP BY {column_name}
            ORDER BY count DESC
            LIMIT %s;
            """
            self.cursor.execute(query, (limit,))
            return self.cursor.fetchall()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def inspect_table(self, table_name):
        """Complete inspection of a table"""
        print(f"\n{'='*80}")
        print(f"📊 TABLE: {table_name.upper()}")
        print(f"{'='*80}\n")
        
        # Table statistics
        stats = self.get_table_stats(table_name)
        print(f"📈 STATISTICS:")
        print(f"   Total Rows: {stats['total_rows']:,}")
        print(f"   Total Size: {stats['total_size']}")
        print(f"   Table Size: {stats['table_size']}")
        print(f"   Indexes Size: {stats['indexes_size']}\n")
        
        # Columns
        columns = self.get_table_columns(table_name)
        print(f"📋 COLUMNS ({len(columns)} total):")
        print(f"{'   ':<3}{'Column Name':<30}{'Data Type':<25}{'Nullable':<10}{'Default':<20}")
        print(f"   {'-'*95}")
        for col in columns:
            col_type = col['data_type']
            if col['character_maximum_length']:
                col_type += f"({col['character_maximum_length']})"
            elif col['numeric_precision']:
                col_type += f"({col['numeric_precision']},{col['numeric_scale']})"
            
            nullable = "YES" if col['is_nullable'] == 'YES' else "NO"
            default = str(col['column_default'])[:18] if col['column_default'] else "-"
            
            print(f"   {col['column_name']:<30}{col_type:<25}{nullable:<10}{default:<20}")
        
        # Primary Keys
        print(f"\n🔑 PRIMARY KEYS:")
        pks = self.get_primary_keys(table_name)
        if pks:
            for pk in pks:
                print(f"   - {pk['column_name']} (constraint: {pk['constraint_name']})")
        else:
            print(f"   No primary keys found")
        
        # Foreign Keys
        print(f"\n🔗 FOREIGN KEYS:")
        fks = self.get_foreign_keys(table_name)
        if fks:
            for fk in fks:
                print(f"   - {fk['column_name']} → {fk['foreign_table_name']}.{fk['foreign_column_name']}")
                print(f"     (constraint: {fk['constraint_name']})")
        else:
            print(f"   No foreign keys found")
        
        # Unique Constraints
        print(f"\n✨ UNIQUE CONSTRAINTS:")
        uniques = self.get_unique_constraints(table_name)
        if uniques:
            for uq in uniques:
                print(f"   - {uq['column_name']} (constraint: {uq['constraint_name']})")
        else:
            print(f"   No unique constraints found")
        
        # Check Constraints
        print(f"\n✓ CHECK CONSTRAINTS:")
        checks = self.get_check_constraints(table_name)
        if checks:
            for chk in checks:
                print(f"   - {chk['constraint_name']}")
                print(f"     {chk['constraint_definition']}")
        else:
            print(f"   No check constraints found")
        
        # Indexes
        print(f"\n📇 INDEXES:")
        indexes = self.get_indexes(table_name)
        if indexes:
            for idx in indexes:
                print(f"   - {idx['indexname']}")
                print(f"     {idx['indexdef']}")
        else:
            print(f"   No indexes found")
        
        # NULL Analysis
        print(f"\n🔍 NULL VALUE ANALYSIS:")
        null_stats = self.get_null_analysis(table_name)
        print(f"   {'Column':<30}{'Total Rows':<15}{'Non-NULL':<15}{'NULL Count':<15}{'NULL %':<10}")
        print(f"   {'-'*85}")
        for stat in null_stats:
            print(f"   {stat['column']:<30}{stat['total_rows']:<15}{stat['non_null_count']:<15}"
                  f"{stat['null_count']:<15}{stat['null_percentage']:<10}%")
        
        # Sample Data
        print(f"\n📝 SAMPLE DATA (First 5 rows):")
        samples = self.get_sample_data(table_name, 5)
        if samples:
            # Show first 3 columns only for readability
            first_cols = list(samples[0].keys())[:3]
            for i, row in enumerate(samples, 1):
                print(f"\n   Row {i}:")
                for col in first_cols:
                    value = str(row[col])[:50] if row[col] else "NULL"
                    print(f"      {col}: {value}")
        
        # Distinct Values for key columns
        print(f"\n🎯 DISTINCT VALUES FOR KEY COLUMNS:")
        key_columns = ['status', 'name', 'department', 'role'] if table_name == 'users' else \
                     ['status'] if table_name in ['checklist', 'delegation'] else []
        
        for col_name in key_columns:
            if any(c['column_name'] == col_name for c in columns):
                print(f"\n   Column: {col_name}")
                distinct = self.get_distinct_values(table_name, col_name, 10)
                if isinstance(distinct, str):
                    print(f"      {distinct}")
                else:
                    for val in distinct:
                        print(f"      - {val['value']}: {val['count']:,} rows")
    
    def export_to_file(self, filename="database_schema_report.txt"):
        """Export complete report to file"""
        import sys
        original_stdout = sys.stdout
        
        with open(filename, 'w', encoding='utf-8') as f:
            sys.stdout = f
            
            print(f"{'='*80}")
            print(f"DATABASE SCHEMA INSPECTION REPORT")
            print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Database: {DB_CONFIG['database']}")
            print(f"Host: {DB_CONFIG['host']}")
            print(f"{'='*80}")
            
            for table in TABLES:
                self.inspect_table(table)
            
            print(f"\n{'='*80}")
            print(f"END OF REPORT")
            print(f"{'='*80}")
        
        sys.stdout = original_stdout
        print(f"\n✅ Report exported to: {filename}")
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("\n✅ Database connection closed")


def main():
    """Main execution"""
    inspector = DatabaseInspector()
    
    if not inspector.connect():
        return
    
    try:
        # Inspect all tables
        for table in TABLES:
            inspector.inspect_table(table)
        
        # Export to file
        print(f"\n{'='*80}")
        export = input("\nExport report to file? (y/n): ").strip().lower()
        if export == 'y':
            filename = input("Enter filename (default: database_schema_report.txt): ").strip()
            if not filename:
                filename = "database_schema_report.txt"
            inspector.export_to_file(filename)
    
    except Exception as e:
        print(f"\n❌ Error during inspection: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        inspector.close()


if __name__ == "__main__":
    main()
