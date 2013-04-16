%define debug_package %{nil}

Summary:	Multimedia player based on mplayer technology
Name:		rosa-media-player
Version:	1.6
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://www.rosalinux.com
Source0:	%{name}-%{version}.tar.gz
Patch0:		rosa-media-player-1.6-set-initialpreference-to-use-by-default.patch
BuildRequires:	qt4-devel	>= 4.2.0
BuildRequires:	qt4-linguist	>= 4.2.0
BuildRequires:	wildmidi-devel
BuilDrequires:	pkgconfig(QJson)
Requires:	mplayer		>= 1.0-1.rc1
Requires:	mencoder
Requires:	ffmpeg
Requires:	xdg-utils
Requires:	timidity-patch-gravis
Requires:	qjson
Requires:	wget
Requires:	libWildMidi.so.1%{_arch_tag_suffix}

%description
Rosa Media Player (ROMP) - multimedia player that supports
most of audio and video formats such as Audio CD, DVD, Video CD,
multimedia files in AVi, ASF/WMV/WMA, MOV/MP4, RealMedia,
Ogg Vorbis, NUT, NSV, VIVO, FLI, NuppelVideo, yuv4mpeg, FILM (.cpk),
RoQ, PVA and Matroska  formats recorded with video codecs - DivX , 
MPEG-1, MPEG-2, MPEG-4, Sorenson, WMV, RealVideo, x264 and audio
codecs MP3, Musepack, Vorbis, RealAudio, AC3/A52 (Dolby Digital),
AAC (MPEG-4 audio), QuickTime, VIVO audio and WMA and many other
less widespread video and audio codecs.

It also supports streaming via HTTP/FTP, RTP/RTSP, MMS/MMST, MPST,
SDP, capture and record (via mencoder) of television signal.

ROMP allows you to trim a particular piece of video, extract audio from
multimedia files and record screen presentations and many other things.

%prep
%setup -qn %{name}
%patch0 -p1 -b .pref~

%build
%setup_compile_flags
./get_romp_version.sh %{version} %{release}
%make PREFIX=%{_prefix} QMAKE=%{qt4bin}/qmake LRELEASE=%{qt4bin}/lrelease

%install
%makeinstall_std PREFIX=%{_prefix}

# remove wrongly put docs
rm -r %{buildroot}%{_datadir}/doc

%files
%doc *.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shortcuts
%dir %{_datadir}/%{name}/translations

%{_bindir}/%{name}

%{_datadir}/%{name}/*.conf
%{_iconsdir}/hicolor/*/apps/rosamp.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/shortcuts/*
%{_datadir}/apps/solid/actions/

%lang(ar_SY) %{_datadir}/%{name}/translations/rosamp_ar_SY.qm
%lang(en) %{_datadir}/%{name}/translations/rosamp_en.qm
%lang(cs) %{_datadir}/%{name}/translations/rosamp_cs.qm
%lang(de) %{_datadir}/%{name}/translations/rosamp_de.qm
%lang(es) %{_datadir}/%{name}/translations/rosamp_es.qm
%lang(et) %{_datadir}/%{name}/translations/rosamp_et.qm
%lang(fi) %{_datadir}/%{name}/translations/rosamp_fi.qm
%lang(fr) %{_datadir}/%{name}/translations/rosamp_fr.qm
%lang(gl) %{_datadir}/%{name}/translations/rosamp_gl.qm
%lang(hu) %{_datadir}/%{name}/translations/rosamp_hu.qm
%lang(it) %{_datadir}/%{name}/translations/rosamp_it.qm
%lang(ja) %{_datadir}/%{name}/translations/rosamp_ja.qm
%lang(ku) %{_datadir}/%{name}/translations/rosamp_ku.qm
%lang(lt) %{_datadir}/%{name}/translations/rosamp_lt.qm
%lang(mk) %{_datadir}/%{name}/translations/rosamp_mk.qm
%lang(nl) %{_datadir}/%{name}/translations/rosamp_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/rosamp_pl.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/rosamp_pt_BR.qm
%lang(pt_pt) %{_datadir}/%{name}/translations/rosamp_pt.qm
%lang(ro_RO) %{_datadir}/%{name}/translations/rosamp_ro_RO.qm
%lang(ru_RU) %{_datadir}/%{name}/translations/rosamp_ru_RU.qm
%lang(sl) %{_datadir}/%{name}/translations/rosamp_sl.qm
%lang(tr) %{_datadir}/%{name}/translations/rosamp_tr.qm
%lang(uk_UA) %{_datadir}/%{name}/translations/rosamp_uk_UA.qm
%lang(vi) %{_datadir}/%{name}/translations/rosamp_vi_VN.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/rosamp_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/rosamp_zh_TW.qm
