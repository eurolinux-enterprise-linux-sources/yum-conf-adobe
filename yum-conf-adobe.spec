Name:           yum-conf-adobe       
Version:        6
Release:        1.2
Summary:        linux.adobe.com Repository Configuration
Group:          System Environment/Base 
License:        BSD 
URL:            http://linuxdownload.adobe.com/
Requires:       adobe-release
BuildArch:      x86_64 i686
%ifarch i686
Requires:	adobe-release-i386
%endif
%ifarch x86_64
Requires:	adobe-release-i386
Requires:	adobe-release-x86_64
%endif
Requires:	yum-plugin-fastestmirror

%description
This package pulls in adobe-release which contains the
linuxdownload.adobe.com yum repository for your architecture.

%files


%changelog
* Tue Dec 6 2011 Pat Riehecky <riehecky@fnal.gov> - 6-1.2
- Added requires yum-plugin-fastest mirror (adding to all non SL yum-conf packages)

* Tue Nov 29 2011 Pat Riehecky <riehecky@fnal.gov> - 6-1.1
- Modified the description and requires so that we can use the 64-bit repo adobe is now providing

* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

