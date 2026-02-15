"""
Test DAG integrity and structure
This test validates that all DAGs can be loaded without errors.
"""
import os
import sys
from pathlib import Path

# Add the dags directory to the Python path
DAGS_DIR = Path(__file__).parent.parent / "dags"
sys.path.insert(0, str(DAGS_DIR))


def test_dag_integrity():
    """Test that all DAG files can be imported without errors"""
    import importlib.util
    
    dag_files = list(DAGS_DIR.glob("*.py"))
    assert len(dag_files) > 0, "No DAG files found"
    
    errors = []
    for dag_file in dag_files:
        if dag_file.name.startswith("__"):
            continue
            
        try:
            spec = importlib.util.spec_from_file_location(dag_file.stem, dag_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"✓ Successfully loaded {dag_file.name}")
        except Exception as e:
            errors.append(f"✗ Error loading {dag_file.name}: {str(e)}")
    
    if errors:
        for error in errors:
            print(error)
        assert False, f"Found {len(errors)} DAG loading error(s)"
    
    print(f"\n✓ All {len(dag_files)} DAG files loaded successfully!")


def test_dag_structure():
    """Test that DAGs have required properties"""
    from airflow.models import DagBag
    
    dagbag = DagBag(dag_folder=str(DAGS_DIR), include_examples=False)
    
    # Check for import errors
    assert len(dagbag.import_errors) == 0, f"DAG import errors: {dagbag.import_errors}"
    
    # Check that we have DAGs
    assert len(dagbag.dags) > 0, "No DAGs found in DagBag"
    
    print(f"\n✓ Found {len(dagbag.dags)} DAG(s):")
    for dag_id, dag in dagbag.dags.items():
        print(f"  - {dag_id}")
        print(f"    Tasks: {len(dag.tasks)}")
        print(f"    Schedule: {dag.schedule_interval}")
        
        # Validate basic DAG properties
        assert dag.dag_id, f"DAG {dag_id} missing dag_id"
        assert len(dag.tasks) > 0, f"DAG {dag_id} has no tasks"
    
    print("\n✓ All DAGs have valid structure!")


if __name__ == "__main__":
    print("Testing DAG integrity...")
    test_dag_integrity()
    print("\nTesting DAG structure...")
    test_dag_structure()
    print("\n✅ All tests passed!")
