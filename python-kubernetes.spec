%global debug_package %{nil}

Name: python-kubernetes
Epoch: 100
Version: 19.15.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python client for the kubernetes API.
License: Apache-2.0
URL: https://github.com/kubernetes-client/python/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package provides a Python client for kubernetes. Kubernetes is a
system for automating deployment, scaling, and management of
containerized applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-kubernetes
Summary: Python client for the kubernetes API.
Requires: python3
Requires: python3-certifi >= 14.05.14
Requires: python3-python-dateutil >= 2.5.3
Requires: python3-google-auth >= 1.0.1
Requires: python3-PyYAML >= 3.12
Requires: python3-requests,
Requires: python3-requests-oauthlib,
Requires: python3-setuptools >= 21.0.0
Requires: python3-six >= 1.9.0
Requires: python3-urllib3 >= 1.24.2
Requires: python3-websocket-client >= 0.32.0
Provides: python3-kubernetes = %{epoch}:%{version}-%{release}
Provides: python3dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(kubernetes) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-kubernetes
This package provides a Python client for kubernetes. Kubernetes is a
system for automating deployment, scaling, and management of
containerized applications.

%files -n python%{python3_version_nodots}-kubernetes
%license LICENSE
%{python3_sitelib}/kubernetes*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-kubernetes
Summary: Python client for the kubernetes API.
Requires: python3
Requires: python3-certifi >= 14.05.14
Requires: python3-python-dateutil >= 2.5.3
Requires: python3-google-auth >= 1.0.1
Requires: python3-PyYAML >= 3.12
Requires: python3-requests,
Requires: python3-requests-oauthlib,
Requires: python3-setuptools >= 21.0.0
Requires: python3-six >= 1.9.0
Requires: python3-urllib3 >= 1.24.2
Requires: python3-websocket-client >= 0.32.0
Provides: python3-kubernetes = %{epoch}:%{version}-%{release}
Provides: python3dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(kubernetes) = %{epoch}:%{version}-%{release}

%description -n python3-kubernetes
This package provides a Python client for kubernetes. Kubernetes is a
system for automating deployment, scaling, and management of
containerized applications.

%files -n python3-kubernetes
%license LICENSE
%{python3_sitelib}/kubernetes*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-kubernetes
Summary: Python client for the kubernetes API.
Requires: python3
Requires: python3-certifi >= 14.05.14
Requires: python3-dateutil >= 2.5.3
Requires: python3-google-auth >= 1.0.1
Requires: python3-pyyaml >= 3.12
Requires: python3-requests,
Requires: python3-requests-oauthlib,
Requires: python3-setuptools >= 21.0.0
Requires: python3-six >= 1.9.0
Requires: python3-urllib3 >= 1.24.2
Requires: python3-websocket-client >= 0.32.0
Provides: python3-kubernetes = %{epoch}:%{version}-%{release}
Provides: python3dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(kubernetes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-kubernetes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(kubernetes) = %{epoch}:%{version}-%{release}

%description -n python3-kubernetes
This package provides a Python client for kubernetes. Kubernetes is a
system for automating deployment, scaling, and management of
containerized applications.

%files -n python3-kubernetes
%license LICENSE
%{python3_sitelib}/kubernetes*
%endif

%changelog
