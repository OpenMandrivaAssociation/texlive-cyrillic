# revision 23396
# category Package
# catalog-ctan /macros/latex/required/cyrillic
# catalog-date 2011-06-16 20:40:55 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-cyrillic
Version:	20110616
Release:	1
Summary:	Support for Cyrillic fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/cyrillic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.source.tar.xz
# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Source3:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.tar.xz
Source4:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-cyrillic-bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This bundle of macros files provides macro support (including
font encoding macros) for the use of Cyrillic characters in
fonts encoded under the T2* and X2 encodings. These encodings
cover (between them) pretty much every language that is written
in a Cyrillic alphabet. This directory is part of the LaTeX
"required" distribution.

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
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_texmfdistdir}/tex/latex/cyrillic/cp1251.def
%{_texmfdistdir}/tex/latex/cyrillic/cp855.def
%{_texmfdistdir}/tex/latex/cyrillic/cp866.def
%{_texmfdistdir}/tex/latex/cyrillic/cp866av.def
%{_texmfdistdir}/tex/latex/cyrillic/cp866mav.def
%{_texmfdistdir}/tex/latex/cyrillic/cp866nav.def
%{_texmfdistdir}/tex/latex/cyrillic/cp866tat.def
%{_texmfdistdir}/tex/latex/cyrillic/ctt.def
%{_texmfdistdir}/tex/latex/cyrillic/dbk.def
%{_texmfdistdir}/tex/latex/cyrillic/iso88595.def
%{_texmfdistdir}/tex/latex/cyrillic/isoir111.def
%{_texmfdistdir}/tex/latex/cyrillic/koi8-r.def
%{_texmfdistdir}/tex/latex/cyrillic/koi8-ru.def
%{_texmfdistdir}/tex/latex/cyrillic/koi8-u.def
%{_texmfdistdir}/tex/latex/cyrillic/lcy.sty
%{_texmfdistdir}/tex/latex/cyrillic/lcyccr.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcycmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcydefs.tex
%{_texmfdistdir}/tex/latex/cyrillic/lcyenc.def
%{_texmfdistdir}/tex/latex/cyrillic/lcylcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/lcylcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/maccyr.def
%{_texmfdistdir}/tex/latex/cyrillic/macukr.def
%{_texmfdistdir}/tex/latex/cyrillic/mik.def
%{_texmfdistdir}/tex/latex/cyrillic/mls.def
%{_texmfdistdir}/tex/latex/cyrillic/mnk.def
%{_texmfdistdir}/tex/latex/cyrillic/mos.def
%{_texmfdistdir}/tex/latex/cyrillic/ncc.def
%{_texmfdistdir}/tex/latex/cyrillic/ot2ccr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2cmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2enc.def
%{_texmfdistdir}/tex/latex/cyrillic/ot2lcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2lcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2wlcyr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2wlcyss.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2wncyr.fd
%{_texmfdistdir}/tex/latex/cyrillic/ot2wncyss.fd
%{_texmfdistdir}/tex/latex/cyrillic/pt154.def
%{_texmfdistdir}/tex/latex/cyrillic/pt254.def
%{_texmfdistdir}/tex/latex/cyrillic/t2accr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2acmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2aenc.def
%{_texmfdistdir}/tex/latex/cyrillic/t2alcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2alcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bccr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2bcmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2benc.def
%{_texmfdistdir}/tex/latex/cyrillic/t2blcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2blcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2cccr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2ccmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2cenc.def
%{_texmfdistdir}/tex/latex/cyrillic/t2clcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/t2clcmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2ccr.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmbr.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmdh.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmfib.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmfr.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmr.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmtl.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2cmvtt.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2enc.def
%{_texmfdistdir}/tex/latex/cyrillic/x2lcmss.fd
%{_texmfdistdir}/tex/latex/cyrillic/x2lcmtt.fd
%doc %{_texmfdistdir}/doc/latex/cyrillic/00readme.txt
%doc %{_texmfdistdir}/doc/latex/cyrillic/changes.txt
%doc %{_texmfdistdir}/doc/latex/cyrillic/cyinpenc.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/cyoutenc.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/lcy.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/lcycmlh.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/manifest.txt
%doc %{_texmfdistdir}/doc/latex/cyrillic/ot2.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/ot2cmams.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/ot2cmlh.pdf
%doc %{_texmfdistdir}/doc/latex/cyrillic/t2lhfnt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cyrillic/cyinpenc.dtx
%doc %{_texmfdistdir}/source/latex/cyrillic/cyoutenc.dtx
%doc %{_texmfdistdir}/source/latex/cyrillic/cyrlatex.ins
%doc %{_texmfdistdir}/source/latex/cyrillic/lcy.dtx
%doc %{_texmfdistdir}/source/latex/cyrillic/lcycmlh.fdd
%doc %{_texmfdistdir}/source/latex/cyrillic/ot2.dtx
%doc %{_texmfdistdir}/source/latex/cyrillic/ot2cmams.fdd
%doc %{_texmfdistdir}/source/latex/cyrillic/ot2cmlh.fdd
%doc %{_texmfdistdir}/source/latex/cyrillic/t2lhfnt.fdd
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2 -a3 -a4

%build

%install
# shell scripts
mkdir -p %{buildroot}%{_bindir}
cp -fa bin/x86_64-linux/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
