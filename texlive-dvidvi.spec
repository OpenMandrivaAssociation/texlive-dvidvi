# revision 23089
# category TLCore
# catalog-ctan /dviware/dvidvi
# catalog-date 2011-02-05 10:39:32 +0100
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-dvidvi
Version:	1.0
Release:	1
Summary:	Convert one DVI file into another
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvidvi
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvidvi.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-dvidvi.bin
Conflicts:	texlive-texmf <= 20110705-3

%description
The output DVI file's contents are specified by page selection
commands; series of pages and page number ranges may be
specified, as well as inclusions and exclusions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/dvidvi.1*
%{_texmfdir}/doc/man/man1/dvidvi.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
