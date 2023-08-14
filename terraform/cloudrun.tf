resource "google_cloud_run_service" "default" {
  name     = "django-app"
  location = "asia-southeast1"

  template {
    spec {
      containers {
        image = "gcr.io/alviandk/django-app:latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

output "cloud_run_url" {
  value = "${google_cloud_run_service.default.status[0].url}"
}
