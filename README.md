# File System MCP Server

This is a FastMCP server that provides basic file system operations within a restricted directory (`fs/`).

## Installation

Install the dependencies using pip:

```bash
uv sync
```

## Running the Server

Run the server with:

```bash
uv run main.py
```

The server communicates via stdio for MCP protocol.

## Tools

### delete

Deletes a specified file from the file system.

**Parameters:**
- `filepath` (string): The full path to the file to delete. The path must start with the root directory to prevent unauthorized access.

**Returns:**
- `bool`: `true` if the file was successfully deleted, `false` otherwise (e.g., file not found, permission denied, or path outside the allowed root).

**Example:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "delete",
    "arguments": {
      "filepath": "/path/to/fs/file.txt"
    }
  }
}
```

### list_files

Lists all files in the root directory.

**Parameters:** None

**Returns:**
- `list[string]`: A list of full paths to files in the root directory.

**Example:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "list_files",
    "arguments": {}
  }
}
```

## Security

The server restricts operations to the `fs/` directory relative to the script's location to prevent unauthorized file access.

# License
MIT
