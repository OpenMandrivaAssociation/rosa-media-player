Summary:	Multimedia player based on mplayer technology
Name:		rosa-media-player
Version:	1.0
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source:		%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel	>= 4.2.0
BuildRequires:	qt4-linguist	>= 4.2.0
Requires:	mplayer		>= 1.0-1.rc1
Requires:	mencoder
Requires:	ffmpeg
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Rosa Media Player (ROMP) - multimedia player that supports most of audio and video formats such as Audio CD, DVD, Video CD,
multimedia files in AVi, ASF/WMV/WMA, MOV/MP4, RealMedia, Ogg Vorbis, NUT, NSV, VIVO, FLI, NuppelVideo, yuv4mpeg, FILM (.cpk),
RoQ, PVA and Matroska  formats recorded with video codecs - DivX , MPEG-1, MPEG-2, MPEG-4, Sorenson, WMV, RealVideo, x264
and audio codecs MP3, Musepack, Vorbis, RealAudio, AC3/A52 (Dolby Digital), AAC (MPEG-4 audio), QuickTime, VIVO audio and WMA
and many other less widespread video and audio codecs. 
It also supports streaming via HTTP/FTP, RTP/RTSP, MMS/MMST, MPST, SDP, capture and record (via mencoder) of television signal.
ROMP allows you to trim a particular piece of video, extract audio from multimedia files and record screen presentations and
many other things.

%prep
%setup -qn %{name}

%build
%setup_compile_flags
%make PREFIX=%{_prefix} QMAKE=%{qt4bin}/qmake LRELEASE=%{qt4bin}/lrelease
# (tpg) don't use kde dialogs
#KDE_SUPPORT=1

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std PREFIX=%{_prefix}

# remove wrongly put docs
rm -rf %{buildroot}%{_datadir}/doc

#desktop-file-install \
#	--remove-key='Encoding' \
#	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#%clean
#[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
#--%defattr(644,root,root,755)
%doc Changelog *.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shortcuts
%dir %{_datadir}/%{name}/translations
%attr(755,root,root) %{_bindir}/%{name}
#%{_mandir}/man1/%{name}.*
%{_datadir}/%{name}/*.conf
%{_iconsdir}/hicolor/*/apps/rosamp.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/shortcuts/*
%lang(ar_SY) %{_datadir}/%{name}/translations/rosamp_ar_SY.qm
%lang(bg) %{_datadir}/%{name}/translations/rosamp_bg.qm
%lang(ca) %{_datadir}/%{name}/translations/rosamp_ca.qm
%lang(cs) %{_datadir}/%{name}/translations/rosamp_cs.qm
%lang(de) %{_datadir}/%{name}/translations/rosamp_de.qm
%lang(el_GR) %{_datadir}/%{name}/translations/rosamp_el_GR.qm
%lang(en_US) %{_datadir}/%{name}/translations/rosamp_en_US.qm
%lang(es) %{_datadir}/%{name}/translations/rosamp_es.qm
%lang(et) %{_datadir}/%{name}/translations/rosamp_et.qm
%lang(eu) %{_datadir}/%{name}/translations/rosamp_eu.qm
%lang(fi) %{_datadir}/%{name}/translations/rosamp_fi.qm
%lang(fr) %{_datadir}/%{name}/translations/rosamp_fr.qm
%lang(gl) %{_datadir}/%{name}/translations/rosamp_gl.qm
%lang(hu) %{_datadir}/%{name}/translations/rosamp_hu.qm
%lang(it) %{_datadir}/%{name}/translations/rosamp_it.qm
%lang(ja) %{_datadir}/%{name}/translations/rosamp_ja.qm
%lang(ka) %{_datadir}/%{name}/translations/rosamp_ka.qm
%lang(ko) %{_datadir}/%{name}/translations/rosamp_ko.qm
%lang(ku) %{_datadir}/%{name}/translations/rosamp_ku.qm
%lang(lt) %{_datadir}/%{name}/translations/rosamp_lt.qm
%lang(mk) %{_datadir}/%{name}/translations/rosamp_mk.qm
%lang(nl) %{_datadir}/%{name}/translations/rosamp_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/rosamp_pl.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/rosamp_pt_BR.qm
%lang(pt_pt) %{_datadir}/%{name}/translations/rosamp_pt.qm
%lang(ro_RO) %{_datadir}/%{name}/translations/rosamp_ro_RO.qm
%lang(ru_RU) %{_datadir}/%{name}/translations/rosamp_ru_RU.qm
%lang(sk) %{_datadir}/%{name}/translations/rosamp_sk.qm
%lang(sl) %{_datadir}/%{name}/translations/rosamp_sl_SI.qm
%lang(sr) %{_datadir}/%{name}/translations/rosamp_sr.qm
%lang(sv) %{_datadir}/%{name}/translations/rosamp_sv.qm
%lang(tr) %{_datadir}/%{name}/translations/rosamp_tr.qm
%lang(uk_UA) %{_datadir}/%{name}/translations/rosamp_uk_UA.qm
%lang(vi) %{_datadir}/%{name}/translations/rosamp_vi_VN.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/rosamp_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/rosamp_zh_TW.qm


