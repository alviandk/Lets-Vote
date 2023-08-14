resource "google_secret_manager_secret" "secret_key" {
  secret_id = "SECRET_KEY"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "secret_key_version" {
  secret      = google_secret_manager_secret.secret_key.name
  secret_data = "your-secret-key"
}

resource "google_secret_manager_secret" "db_name" {
  secret_id = "DB_NAME"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "db_name_version" {
  secret      = google_secret_manager_secret.db_name.name
  secret_data = "your-database-name"
}

resource "google_secret_manager_secret" "db_user" {
  secret_id = "DB_USER"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "db_user_version" {
  secret      = google_secret_manager_secret.db_user.name
  secret_data = "your-database-user"
}

resource "google_secret_manager_secret" "db_password" {
  secret_id = "DB_PASSWORD"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "db_password_version" {
  secret      = google_secret_manager_secret.db_password.name
  secret_data = "your-database-password"
}

resource "google_secret_manager_secret" "db_host" {
  secret_id = "DB_HOST"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "db_host_version" {
  secret      = google_secret_manager_secret.db_host.name
  secret_data = "your-database-host"
}

resource "google_secret_manager_secret" "db_port" {
  secret_id = "DB_PORT"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "db_port_version" {
  secret      = google_secret_manager_secret.db_port.name
  secret_data = "your-database-port"
}

# Output the names of the created secrets for reference
output "secrets" {
  description = "Names of the secrets created for the application"
  value = {
    SECRET_KEY   = google_secret_manager_secret.secret_key.name
    DB_NAME      = google_secret_manager_secret.db_name.name
    DB_USER      = google_secret_manager_secret.db_user.name
    DB_PASSWORD  = google_secret_manager_secret.db_password.name
    DB_HOST      = google_secret_manager_secret.db_host.name
    DB_PORT      = google_secret_manager_secret.db_port.name
  }
}
