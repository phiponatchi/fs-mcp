import os
from pathlib import Path

from fastmcp import FastMCP

root = f"{Path(__file__).resolve().parent}/fs/"
print(f"Root directory: {root}", file=os.sys.stderr)


mcp = FastMCP("File System")

@mcp.tool(
    name="delete_file",
    description="Delete a file from the file system"
)
def delete(filepath: str) -> bool:
    """Delete a file from the file system.

    Args:
        filepath (str): The full path to the file to delete. Must be within the allowed root directory.

    Returns:
        bool: True if the file was successfully deleted, False otherwise (e.g., file not found, permission denied, or path outside root).
    """
    if not filepath or not filepath.startswith(root):
        return False
    try:
        os.remove(filepath)
        return True
    except Exception as e:
        print(f"Error occurred while deleting file: {e}", file=os.sys.stderr)
        return False

@mcp.tool(
    name="list_files",
    description="List of files in the file system"
)
def list_files() -> list[str]:
    """List all files in the root directory.

    Returns:
        list[str]: A list of full paths to files in the root directory.
    """
    files = os.listdir(root)
    return [root + file for file in files]

if __name__ == "__main__":
    mcp.run(transport='stdio')