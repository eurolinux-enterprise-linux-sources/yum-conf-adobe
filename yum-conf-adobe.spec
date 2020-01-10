Name:           yum-conf-adobe       
Version:        6
Release:        1
Summary:        linux.adobe.com Repository Configuration
Group:          System Environment/Base 
License:        BSD 
URL:            http://linuxdownload.adobe.com/
Requires:       adobe-release-i386

%description
This package pulls in adobe-release-i386 which contains the
linuxdownload.adobe.com yum repository.

%files


%changelog
* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

