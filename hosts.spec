Name: check-hosts
Version: 1.0
Release: 1%{?dist}
Summary: Script to check availability of a list of hosts
License: GPL
Group: Networking/Tools
BuildArch: noarch
Requires: bash, iputils

%description
This package provides a script to check the availability of a list of hosts provided by the user.
It uses ping to verify if the hosts are reachable.

%prep
# Подготовительный этап, здесь можно добавить команды, если нужно

%build
# Сборка не требуется для скрипта на bash

%install
# Создаем целевую директорию для установки и копируем туда скрипт
mkdir -p %{buildroot}/usr/local/bin
cp check_hosts.sh %{buildroot}/usr/local/bin/check-hosts
chmod +x %{buildroot}/usr/local/bin/check-hosts

%files
/usr/local/bin/check-hosts

%changelog
* Tue Oct 30 2024 Your Name <your.email@example.com> - 1.0-1
- Initial release of check-hosts script
