Name:		texlive-cyrillic
Version:	20180408
Release:	1
Summary:	Support for Cyrillic fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/cyrillic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cyrillic-bin

%description
This bundle of macros files provides macro support (including
font encoding macros) for the use of Cyrillic characters in
fonts encoded under the T2* and X2 encodings. These encodings
cover (between them) pretty much every language that is written
in a Cyrillic alphabet. This directory is part of the LaTeX
"required" distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cyrillic
%doc %{_texmfdistdir}/doc/latex/cyrillic
#- source
%doc %{_texmfdistdir}/source/latex/cyrillic

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
