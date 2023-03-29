import docker
import os 



## running the scan


try:
    build_dir = os.getcwd()
    docker_image = 'owasp/zap2docker-stable '
    command_line = 'touch /zap/wrk/ramanuja.txt'
    user = 'jenkins'
    vol = '/zap/wrk'
    container_output = docker.containers.run(docker_image, command_line, volumes={build_dir: {
                    'bind': , 'mode': 'rw'}},user=user)
    print('[SUCCESS]: Scan Completed aranga')
    print(container_output)
except errors.ContainerError as exc:
    print('%s',str(exc))   
