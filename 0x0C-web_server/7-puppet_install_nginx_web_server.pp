# Install Nginx
class nginx {
  package { 'nginx':
    ensure => installed,
  }
}

# Configure Nginx server
class nginx::config {
  # Configure Nginx to listen on port 80
  file { '/etc/nginx/sites-available/default':
    ensure => file,
    content => "
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;

  server_name _;

  location / {
    # Return 'Hello World!' on GET request to /
    if ($request_method = 'GET') {
      add_header Content-Type text/html;
      return 200 'Hello World!';
    }
  }

  # Redirect /redirect_me to /
  location /redirect_me {
    return 301 /;
  }
}
",
    notify => Service['nginx'],
  }

  # Remove default Nginx welcome page
  file { '/var/www/html/index.nginx-debian.html':
    ensure => absent,
  }

  # Create a placeholder index.html file
  file { '/var/www/html/index.html':
    ensure => file,
    content => 'This is the default index.html file',
  }

  # Enable the default site
  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
    notify => Service['nginx'],
  }
}

# Restart Nginx
class nginx::service {
  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

# Apply classes to node
node default {
  include nginx
  include nginx::config
  include nginx::service
}

