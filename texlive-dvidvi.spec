# revision 33736
# category TLCore
# catalog-ctan /dviware/dvidvi
# catalog-date 2012-05-07 18:30:58 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-dvidvi
Version:	1.0
Release:	11
Summary:	Convert one DVI file into another
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvidvi
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvidvi.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-dvidvi.bin

%description
The output DVI file's contents are specified by page selection
commands; series of pages and page number ranges may be
specified, as well as inclusions and exclusions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/dvidvi.1*
%{_texmfdistdir}/doc/man/man1/dvidvi.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
