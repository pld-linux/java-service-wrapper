#
# TODO:
# - Is it possible to build it for other archs?
# - BRs

%define ver 3.3.2
%define ver_patch b

%include	/usr/lib/rpm/macros.java
Summary:	Java Service Wrapper
Name:		java-service-wrapper
Version:	%{ver}_%{ver_patch}
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Java
Source0:	http://wrapper.tanukisoftware.org/download/%{ver}-%{ver_patch}/wrapper_%{ver}-%{ver_patch}_src.tar.gz
# Source0-md5:	20529639806b9ccba33281152073e3cb
URL:		http://wrapper.tanukisoftware.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86}
%define bits 32
%endif

%ifarch %{x8664}
%define bits 64
%endif

%description
Java Service Wrapper helps to run java daemon as System V services.

%prep
%setup -q -n wrapper_%{ver}-%{ver_patch}_src

%build
export JAVA_HOME="%{java_home}"

%ant -Dbits=%{bits}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_javadir},%{_sysconfdir}/%{name},%{_sbindir}}

install bin/wrapper $RPM_BUILD_ROOT%{_sbindir}/%{name}
install lib/libwrapper.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libwrapper.so

# jars
cp -a lib/wrapper.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_libdir}/%{name}/libwrapper.so
%doc doc/* conf/wrapper.conf
