Summary:	The uniform password-checking interface
Summary(pl):	Jednolite miêdzymordzie do hase³
Name:		checkpassword
Version:	0.90
Release:	1
License:	Qmail
Group:		Applications/System
Source0:	http://cr.yp.to/checkpwd/%{name}-%{version}.tar.gz
# Source0-md5:	e75842e908f96571ae56c3da499ba1fc
Patch0:		http://qmail.obeer.com/%{name}-pam-0.90.diff.gz
Patch1:		%{name}-pam-pld.patch
URL:		http://cr.yp.to/checkpwd.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
checkpassword provides a simple, uniform password-checking interface
to all root applications. It is suitable for use by applications such
as login, ftpd, and pop3d.

There are checkpassword-compatible tools that support alternate
password databases, secret login names, long passwords, subaccounts,
one-time passwords, detailed accounting, and many other features.
Applications that use the checkpassword interface will work with all
of these tools. Several tools have been specifically designed to
support POP toasters.

%description -l pl
Jednolite miêdzymordzie do hase³, do u¿ycia przez serwery takie jak
ftpd, pop3, imapd, login. Wyposa¿one dodatkowo w ³atkê umo¿liwiaj±c±
wspó³dzia³anie z bibliotek± PAM.

%prep
%setup -q

%patch0 -p1
%patch1

%build
echo '%{__cc} %{rpmcflags}' > conf-cc
echo '%{_prefix}' > conf-home
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install checkpassword $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
