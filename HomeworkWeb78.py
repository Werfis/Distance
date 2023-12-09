from docker import Client
from docker.models.containers import Container
from docker.utils.ports import parse_port
client = Client()
compose = client.load_docker_compose()
container = Container.get("web78", compose)
container.start()
ip, port = parse_port(container.get("ports"))
print(f"Контейнер запущен на локальном IP-адресе: {ip} и порту: {port}")