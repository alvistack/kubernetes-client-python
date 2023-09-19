# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-kubernetes
Epoch: 100
Version: 26.1.0
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

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
%{python3_sitelib}/*
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
%{python3_sitelib}/*
%endif

%if 0%{?centos_version} == 700
%package -n python3-kubernetes
Summary: Python client for the kubernetes API.
Requires: python3
Requires: python3-certifi >= 14.05.14
Requires: python36-dateutil >= 2.5.3
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
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?centos_version} == 700)
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
%{python3_sitelib}/*
%endif

%changelog
