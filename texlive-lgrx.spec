# revision 27003
# category Package
# catalog-ctan /macros/latex/contrib/lgrx
# catalog-date 2012-07-05 15:34:29 +0200
# catalog-license lppl1.3
# catalog-version 0.6
Name:		texlive-lgrx
Epoch:		1
Version:	0.6
Release:	4
Summary:	Greek text with the LGR font encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lgrx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgrx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lgrx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LGRx bundle provides packages and definitions for
typesetting Greek text with fonts in the LGR encoding, the de-
facto standard set by babel. It includes a comprehensive font
definition file, support for Unicode input and macros for Greek
letters in non-Greek text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lgrx/alphabeta.sty
%{_texmfdistdir}/tex/latex/lgrx/lgrenc.dfu
%{_texmfdistdir}/tex/latex/lgrx/lgrxenc.def
%{_texmfdistdir}/tex/latex/lgrx/textalpha.sty
%doc %{_texmfdistdir}/doc/latex/lgrx/README
%doc %{_texmfdistdir}/doc/latex/lgrx/README.html
%doc %{_texmfdistdir}/doc/latex/lgrx/alphabeta-test.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/alphabeta-test.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/alphabeta.sty.html
%doc %{_texmfdistdir}/doc/latex/lgrx/greek-unicode.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/greek-unicode.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/greekhyperref.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/greekhyperref.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrenc.dfu.html
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrx.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrx.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrxenc-test.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrxenc-test.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrxenc.def.html
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrxenc.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/lgrxenc.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/textalpha-test.pdf
%doc %{_texmfdistdir}/doc/latex/lgrx/textalpha-test.tex
%doc %{_texmfdistdir}/doc/latex/lgrx/textalpha.sty.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
