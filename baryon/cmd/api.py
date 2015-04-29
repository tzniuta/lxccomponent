from baryon import service


def main():
    launcher = service.process_launcher()
    server = service.WSGIServiceFactory.getinstance('api')
    launcher.launch_service(server, 1)
    launcher.wait()