resource "google_sql_database_instance" "default" {
  name             = "django-db"
  database_version = "POSTGRES_15"
  region           = "asia-southeast1"
  deletion_protection = false

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "default" {
  name       = "django"
  instance   = google_sql_database_instance.default.name
  collation  = "en_US.UTF8"
}
