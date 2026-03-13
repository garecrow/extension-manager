%global app_id com.mattjakeman.ExtensionManager

Name:           extension-manager
Version:        0.6.5
Release:        %autorelease
Summary:        A utility for browsing and installing GNOME Shell Extensions

License:        GPL-3.0-or-later
URL:            https://github.com/mjakeman/extension-manager
# COPR's SCM mode will replace this with the generated git tarball
Source0:        %{url}/archive/master/extension-manager-master.tar.gz

# This is a C project, so we need a compiler
BuildRequires:  gcc
BuildRequires:  meson >= 0.59.0
BuildRequires:  ninja-build
BuildRequires:  blueprint-compiler
BuildRequires:  gettext

# Core library dependencies mapped from src/meson.build
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)

# Optional backtrace support
BuildRequires:  libbacktrace-devel

# UI Template and Introspection requirements
BuildRequires:  gobject-introspection-devel

# Post-install and validation tools
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gtk4
Requires:       libadwaita

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

%prep
%autosetup -n extension-manager-master

%build
%meson
%meson_build

%install
%meson_install
%find_lang extension-manager

%files -f extension-manager.lang
%license COPYING
%doc README.md
%{_bindir}/extension-manager
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/%{app_id}.metainfo.xml

%changelog
%autochangelog
