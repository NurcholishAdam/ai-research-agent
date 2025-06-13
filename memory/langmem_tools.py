from langmem import create_manage_memory_tool, create_search_memory_tool

def get_memory_tools():
    manage_tool = create_manage_memory_tool(name="save_memory")
    search_tool = create_search_memory_tool(name="search_memory")
    return [manage_tool, search_tool]

