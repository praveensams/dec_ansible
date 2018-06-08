- hosts: localhost
  tasks:
    - name: Test that my module works
      github_repo: 
      register: result

    - debug: var=result


    - name: prock
      proc:
        name: "sam"
      register: result1


    - debug: var=result1
