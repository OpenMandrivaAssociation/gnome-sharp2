%define oname gnome-sharp
%define mono 1.0.2
%define gtk_sharp 2.12.1
%define monodir %{_prefix}/lib/mono

Summary:	C# language binding for GNOME
Name:		gnome-sharp2
Version:	2.24.2
Release:	5
License:	LGPLv2
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-sharp/%oname-%version.tar.bz2
BuildRequires:	mono-devel >= %{mono}
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}

%description
This is a C# language binding for GNOME.

%package 2.4
Summary:	C# language binding for GNOME 2.4
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{name} < 2.24.2-3

%description 2.4
This is a C# language binding for GNOME 2.4.

%package 2.6
Summary:	C# language binding for GNOME 2.6
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{name} < 2.24.2-3

%description 2.6
This is a C# language binding for GNOME 2.6.

%package 2.8
Summary:	C# language binding for GNOME 2.8
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{name} < 2.24.2-3

%description 2.8
This is a C# language binding for GNOME 2.8.

%package 2.16
Summary:	C# language binding for GNOME 2.16
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{name} < 2.24.2-3

%description 2.16
This is a C# language binding for GNOME 2.16.

%package 2.20
Summary:	C# language binding for GNOME 2.20
Group:		System/Libraries
Requires:	%{name} = %{version}
Conflicts:	%{name} < 2.24.2-3

%description 2.20
This is a C# language binding for GNOME 2.20.

%package devel
Summary:	C# language binding for GNOME - devel files
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	gtk-sharp2-devel

%description devel
This is a C# language binding for GNOME. It contains all files that are needed
to build against %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

%files
%doc README
%{_libdir}/libgnomesharpglue-2.so
%{monodir}/gtk-sharp-2.0/art-sharp.dll
%{monodir}/gtk-sharp-2.0/gconf-sharp-peditors.dll
%{monodir}/gtk-sharp-2.0/gconf-sharp.dll
%{monodir}/gtk-sharp-2.0/gnome-sharp.dll
%{monodir}/gtk-sharp-2.0/gnome-vfs-sharp.dll
%{monodir}/gac/art-sharp/2.24.0.0*
%{monodir}/gac/gconf-sharp-peditors/2.24.0.0*
%{monodir}/gac/gconf-sharp/2.24.0.0*
%{monodir}/gac/gnome-sharp/2.24.0.0*
%{monodir}/gac/gnome-vfs-sharp/2.24.0.0*

%files 2.4
%{monodir}/gtk-sharp-2.0/policy.2.4.*.dll
%{monodir}/gac/policy.2.4.*

%files 2.6
%{monodir}/gtk-sharp-2.0/policy.2.6.*.dll
%{monodir}/gac/policy.2.6.*

%files 2.8
%{monodir}/gtk-sharp-2.0/policy.2.8.*.dll
%{monodir}/gac/policy.2.8.*

%files 2.16
%{monodir}/gtk-sharp-2.0/policy.2.16.*.dll
%{monodir}/gac/policy.2.16.*

%files 2.20
%{monodir}/gtk-sharp-2.0/policy.2.20.*.dll
%{monodir}/gac/policy.2.20.*

%files devel
%doc ChangeLog
%doc sample
%{_bindir}/gconfsharp2-schemagen
%{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_datadir}/gapi-2.0/*.xml
%{_libdir}/pkgconfig/art-sharp-2.0.pc
%{_libdir}/pkgconfig/gconf-sharp-2.0.pc
%{_libdir}/pkgconfig/gconf-sharp-peditors-2.0.pc
%{_libdir}/pkgconfig/gnome-vfs-sharp-2.0.pc
%{_libdir}/pkgconfig/gnome-sharp-2.0.pc


%changelog
* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 2.24.2-4mdv2012.0
+ Revision: 741013
- update build deps, we need the OLD gnome panel
- rebuild for gtk+ packaging breakage

* Wed May 04 2011 Funda Wang <fwang@mandriva.org> 2.24.2-3
+ Revision: 665681
- split compat package, gnome# only provides default api version now

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.24.2-2
+ Revision: 664884
- mass rebuild

* Sat Oct 09 2010 Götz Waschk <waschk@mandriva.org> 2.24.2-1mdv2011.0
+ Revision: 584487
- update to new version 2.24.2

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.24.1-2mdv2010.1
+ Revision: 521490
- rebuilt for 2010.1

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 348079
- update to new version 2.24.1

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 282694
- new version

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273544
- new version
- update license

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.20.1-2mdv2009.0
+ Revision: 264558
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2009.0
+ Revision: 196735
- new version
- bump deps

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 2.20.0-5mdv2009.0
+ Revision: 193608
- fix devel deps

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 2.20.0-4mdv2009.0
+ Revision: 192404
- split out devel package

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-3mdv2008.1
+ Revision: 190014
- do not package big ChangeLog
- remove 300k of docs from livecd

* Wed Mar 05 2008 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.1
+ Revision: 179631
- new version
- bump deps

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.1
+ Revision: 159558
- new version
- drop patch

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.19.90-2mdv2008.1
+ Revision: 159333
- add back MasterClient symbol

* Fri Jan 25 2008 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.1
+ Revision: 157867
- new version
- drop patch
- bump deps
- remove libs that are now in gnome-desktop-sharp

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Adam Williamson <awilliamson@mandriva.org> 2.16.0-6mdv2008.1
+ Revision: 105671
- buildrequires gtk-sharp2-devel
- rebuild for 2008
- new license policy
- small spec clean


* Mon Mar 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.16.0-5mdv2007.1
+ Revision: 146583
- split out doc

* Tue Mar 13 2007 Götz Waschk <waschk@mandriva.org> 2.16.0-4mdv2007.1
+ Revision: 143213
- update for gtkhtml 3.14

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.16.0-3mdv2007.1
+ Revision: 126123
- fix gtkhtml dep and major

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
+ Revision: 122687
- fix buildrequires
- Import gnome-sharp2

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- bump deps
- drop the patch
- fix source URL
- New release 2.16.0

* Sat Aug 12 2006 Emmanuel Andry <eandry@mandriva.org> 2.15.0-2mdv2007.0
- statically set /usr/lib to fix packaging on x86_64

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.0-1mdv2007.0
- initial package

