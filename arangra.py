import docker
import os 
from docker import errors

try:
    docker = docker.from_env()
except Exception as e:
    print('Docker not found in your machine, Pls install')
        #print(str(e))
    exit(3) ## docker/system error

    
    
## running the scan


try:
    build_dir = os.getcwd()
    docker_image = 'owasp/zap2docker-stable'
    command_line = 'touch /zap/wrk/ramanuja.txt'
    uid = os.getuid()
    gid = os.getgid()
    userid= f"{uid}:{gid}"
    vol = '/zap/wrk'
    container_output = docker.containers.run(docker_image, command_line, volumes={build_dir: {
                    'bind':vol , 'mode': 'rw'}},user='root')
    print('[SUCCESS]: Scan Completed aranga')
    print(container_output)
except errors.ContainerError as exc:
    print('%s',str(exc))   
