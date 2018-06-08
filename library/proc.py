from ansible.module_utils.basic import *
from subprocess import * 
from sys import *

k='ps aux | grep bash'.split()

def test():
    
    try: 
        s=Popen("ps aux | grep -i bash",shell=True,stdout=PIPE)
        i=s.communicate()[0]
        return(i)
    
    except Exception as e:
      
        return(e)
    

def main():
  # The AnsibleModule provides lots of common code for handling returns, parses your arguments for you, and allows you to check inputs
    module = AnsibleModule(
        argument_spec=dict(
        name=dict(required=True, type='string')
        ),
        supports_check_mode=True
       )

  # in check mode we take no action
  # since this module actually never changes system state we'll just return False
    if module.check_mode:
        module.exit_json(changed=False)

    name = module.params['name']

    if test('name'):
        module.exit_json(changed=False)
    else:
        msg="error in command"
        module.fail_json(msg=msg)

if __name__ == '__main__':
    main()
      
