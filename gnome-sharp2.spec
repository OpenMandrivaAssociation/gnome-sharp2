%define	name	gnome-sharp2
%define oname	gnome-sharp
%define version	2.16.0
%define release	%mkrel 6
%define mono	1.0.2
%define monodir	%_prefix/lib/mono

Summary:	C# language binding for GNOME
Name:		%name
Version:	%version
Release:	%release
License:	LGPLv2
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-sharp/%oname-%version.tar.bz2
Patch:		gnome-sharp-2.16.0-gtkhtml19.patch
BuildRequires:	mono-devel >= %mono
BuildRequires:	libglade2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libGConf2-devel
BuildRequires:	librsvg-devel
BuildRequires:	libgtkhtml-3.14-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	vte-devel
BuildRequires:	gtk-sharp2 >= 2.10.0
BuildRequires:	gtk-sharp2-devel >= 2.10.0
BuildRequires:	glade-sharp2 >= 2.10.0
Requires:	%mklibname gtkhtml-3.14_ 19
Requires:	%mklibname vte 9

%description
Gtk-sharp is a C# language binding for GNOME.


%package doc
Summary:	Documentation for gnome-sharp
Group:		Development/Other

%description doc
Gnome-sharp is a C# language binding for the gnome toolkit.
This package provides documentation for gnome-sharp. 

%prep
rm -rf %buildroot

%setup -q -n %oname-%version
%patch -p1 -b .gtkhtml19
autoconf

%build
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall

rm -rf %buildroot%_libdir/lib*a

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc README
%_bindir/gconfsharp2-schemagen
/usr/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%monodir/gac/*art-sharp
%monodir/gtk-sharp-2.0/*art-sharp.dll*
%_libdir/pkgconfig/art-sharp-2.0.pc
%monodir/gac/*gconf-sharp
%monodir/gac/*gconf-sharp-peditors
%monodir/gac/*gnome-sharp
%monodir/gac/*gtkhtml-sharp
%monodir/gac/*rsvg-sharp
%monodir/gac/*vte-sharp
%monodir/gac/*gnome-vfs-sharp
%monodir/gtk-sharp-2.0/*gconf-sharp.dll*
%monodir/gtk-sharp-2.0/*gconf-sharp-peditors.dll*
%monodir/gtk-sharp-2.0/*gnome-sharp.dll*
%monodir/gtk-sharp-2.0/*gtkhtml-sharp.dll*
%monodir/gtk-sharp-2.0/*rsvg-sharp.dll*
%monodir/gtk-sharp-2.0/*vte-sharp.dll*
%monodir/gtk-sharp-2.0/*gnome-vfs-sharp.dll*
%_libdir/pkgconfig/gconf-sharp-2.0.pc
%_libdir/pkgconfig/gnome-vfs-sharp-2.0.pc
%_libdir/pkgconfig/gnome-sharp-2.0.pc
%_libdir/pkgconfig/gtkhtml-sharp-2.0.pc
%_libdir/pkgconfig/rsvg-sharp-2.0.pc
%_libdir/pkgconfig/vte-sharp-2.0.pc
%_libdir/libgnomesharpglue-2.so
%_libdir/libvtesharpglue-2.so
%_datadir/gapi-2.0/*.xml

%files doc
%defattr(-,root,root)
%doc ChangeLog 
%doc sample

