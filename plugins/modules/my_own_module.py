#!/usr/bin/python

# Copyright: (c) 2024, Your Name <your@email.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with specified content

version_added: "1.0.0"

description:
    - This module creates a text file on the remote host.
    - The file path is specified by the C(path) parameter.
    - The file content is specified by the C(content) parameter.

options:
    path:
        description: Path to the file to create.
        required: true
        type: path
    content:
        description: Content to write to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/test.txt
    content: "Hello, World!"

- name: Create another file
  my_own_module:
    path: /tmp/another.txt
    content: "Another content"
'''

RETURN = r'''
path:
    description: Path to the created file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: Content written to the file.
    type: str
    returned: always
    sample: 'Hello, World!'
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    # Check mode
    if module.check_mode:
        result['path'] = path
        result['content'] = content
        # Check if file exists and content matches
        if os.path.exists(path):
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                module.exit_json(**result)
        result['changed'] = True
        module.exit_json(**result)

    # Check if file exists and content matches (idempotency)
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing_content = f.read()
        if existing_content == content:
            result['path'] = path
            result['content'] = content
            module.exit_json(**result)

    # Create or update file
    try:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
        result['path'] = path
        result['content'] = content
    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
