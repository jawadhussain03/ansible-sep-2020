#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello( message ):
    return "Hello " + message + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str')
        )
    )
    message = module.params['msg']

    output = sayHello( message )

  # module.exit_json(message=output, changed=False)
    module.fail_json(msg="Some error occurred")

if __name__ == '__main__':
    main()
