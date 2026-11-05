# Ansible Collection - my_own_namespace.yandex_cloud_elk

Documentation for the collection.
# my_own_namespace.yandex_cloud_elk

Collection with custom Ansible module for creating text files.

## Modules

### my_own_module

Creates a text file on the remote host with specified content.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | path | yes | Path to the file to create |
| `content` | str | yes | Content to write to the file |

**Example:**

```yaml
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello, World!"
