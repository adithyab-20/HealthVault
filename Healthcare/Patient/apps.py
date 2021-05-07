from django.apps import AppConfig


class PatientConfig(AppConfig):
    name = 'Patient'

    def ready(self):
        import Patient.signals