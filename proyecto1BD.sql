PGDMP                         y            proyecto1BD    13.1    13.1 4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17650    proyecto1BD    DATABASE     m   CREATE DATABASE "proyecto1BD" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Guatemala.1252';
    DROP DATABASE "proyecto1BD";
                postgres    false            ?            1259    17827    album    TABLE     ?   CREATE TABLE public.album (
    albumid integer NOT NULL,
    title character varying(50) NOT NULL,
    artistid integer NOT NULL,
    modify character varying(50)
);
    DROP TABLE public.album;
       public         heap    postgres    false            ?            1259    17795    artist    TABLE     ?   CREATE TABLE public.artist (
    artistid integer NOT NULL,
    name character varying(50) NOT NULL,
    modify character varying(50)
);
    DROP TABLE public.artist;
       public         heap    postgres    false            ?            1259    17667    genre    TABLE     e   CREATE TABLE public.genre (
    genreid integer NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.genre;
       public         heap    postgres    false            ?            1259    17723    modify_album    TABLE     `   CREATE TABLE public.modify_album (
    userid integer NOT NULL,
    albumid integer NOT NULL
);
     DROP TABLE public.modify_album;
       public         heap    postgres    false            ?            1259    17726    modify_artist    TABLE     b   CREATE TABLE public.modify_artist (
    userid integer NOT NULL,
    artistid integer NOT NULL
);
 !   DROP TABLE public.modify_artist;
       public         heap    postgres    false            ?            1259    17729    modify_track    TABLE     ?   CREATE TABLE public.modify_track (
    userid integer NOT NULL,
    trackid integer NOT NULL,
    trackstate character varying(10) NOT NULL
);
     DROP TABLE public.modify_track;
       public         heap    postgres    false            ?            1259    17762    permissions    TABLE     %  CREATE TABLE public.permissions (
    permissionid integer NOT NULL,
    add_artist character varying(5) NOT NULL,
    add_track character varying(5) NOT NULL,
    add_album character varying(5) NOT NULL,
    inactivate_track character varying(5) NOT NULL,
    update_track character varying(5) NOT NULL,
    delete_track character varying(5) NOT NULL,
    update_artist character varying(5) NOT NULL,
    delete_artist character varying(5) NOT NULL,
    delete_album character varying(5) NOT NULL,
    update_album character varying(5) NOT NULL
);
    DROP TABLE public.permissions;
       public         heap    postgres    false            ?            1259    17803    playlist    TABLE     ?   CREATE TABLE public.playlist (
    playlistid integer NOT NULL,
    name character varying(50) NOT NULL,
    modify character varying(50)
);
    DROP TABLE public.playlist;
       public         heap    postgres    false            ?            1259    17715    playlisttrack    TABLE     e   CREATE TABLE public.playlisttrack (
    playlistid integer NOT NULL,
    trackid integer NOT NULL
);
 !   DROP TABLE public.playlisttrack;
       public         heap    postgres    false            ?            1259    17707    role_permission    TABLE     ?   CREATE TABLE public.role_permission (
    role_permissionid integer NOT NULL,
    permissionid integer NOT NULL,
    roleid integer NOT NULL
);
 #   DROP TABLE public.role_permission;
       public         heap    postgres    false            ?            1259    17699    roles    TABLE     d   CREATE TABLE public.roles (
    roleid integer NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.roles;
       public         heap    postgres    false            ?            1259    17683    track    TABLE     ?   CREATE TABLE public.track (
    trackid integer NOT NULL,
    name character varying(50) NOT NULL,
    albumid integer NOT NULL,
    genreid integer NOT NULL,
    composer character varying(50) NOT NULL,
    artistid integer NOT NULL
);
    DROP TABLE public.track;
       public         heap    postgres    false            ?            1259    17651    users    TABLE     ?   CREATE TABLE public.users (
    userid integer NOT NULL,
    name character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    suscribe boolean NOT NULL,
    roleid integer
);
    DROP TABLE public.users;
       public         heap    postgres    false            ?          0    17827    album 
   TABLE DATA           A   COPY public.album (albumid, title, artistid, modify) FROM stdin;
    public          postgres    false    212   %=       ?          0    17795    artist 
   TABLE DATA           8   COPY public.artist (artistid, name, modify) FROM stdin;
    public          postgres    false    210   />       ?          0    17667    genre 
   TABLE DATA           .   COPY public.genre (genreid, name) FROM stdin;
    public          postgres    false    201   ?       ?          0    17723    modify_album 
   TABLE DATA           7   COPY public.modify_album (userid, albumid) FROM stdin;
    public          postgres    false    206   ??       ?          0    17726    modify_artist 
   TABLE DATA           9   COPY public.modify_artist (userid, artistid) FROM stdin;
    public          postgres    false    207   ??       ?          0    17729    modify_track 
   TABLE DATA           C   COPY public.modify_track (userid, trackid, trackstate) FROM stdin;
    public          postgres    false    208   @       ?          0    17762    permissions 
   TABLE DATA           ?   COPY public.permissions (permissionid, add_artist, add_track, add_album, inactivate_track, update_track, delete_track, update_artist, delete_artist, delete_album, update_album) FROM stdin;
    public          postgres    false    209   /@       ?          0    17803    playlist 
   TABLE DATA           <   COPY public.playlist (playlistid, name, modify) FROM stdin;
    public          postgres    false    211   b@       ?          0    17715    playlisttrack 
   TABLE DATA           <   COPY public.playlisttrack (playlistid, trackid) FROM stdin;
    public          postgres    false    205   ?@       ?          0    17707    role_permission 
   TABLE DATA           R   COPY public.role_permission (role_permissionid, permissionid, roleid) FROM stdin;
    public          postgres    false    204   A       ?          0    17699    roles 
   TABLE DATA           -   COPY public.roles (roleid, name) FROM stdin;
    public          postgres    false    203   +A       ?          0    17683    track 
   TABLE DATA           T   COPY public.track (trackid, name, albumid, genreid, composer, artistid) FROM stdin;
    public          postgres    false    202   lA       ?          0    17651    users 
   TABLE DATA           I   COPY public.users (userid, name, password, suscribe, roleid) FROM stdin;
    public          postgres    false    200   G       a           2606    18094    album album_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.album
    ADD CONSTRAINT album_pkey PRIMARY KEY (albumid);
 :   ALTER TABLE ONLY public.album DROP CONSTRAINT album_pkey;
       public            postgres    false    212            ]           2606    18101    artist artist_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (artistid);
 <   ALTER TABLE ONLY public.artist DROP CONSTRAINT artist_pkey;
       public            postgres    false    210            S           2606    18144    genre genre_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (genreid);
 :   ALTER TABLE ONLY public.genre DROP CONSTRAINT genre_pkey;
       public            postgres    false    201            [           2606    18162    permissions permissions_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (permissionid);
 F   ALTER TABLE ONLY public.permissions DROP CONSTRAINT permissions_pkey;
       public            postgres    false    209            _           2606    18174    playlist playlist_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_pkey PRIMARY KEY (playlistid);
 @   ALTER TABLE ONLY public.playlist DROP CONSTRAINT playlist_pkey;
       public            postgres    false    211            Y           2606    18194 &   role_permission roles_permissions_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY public.role_permission
    ADD CONSTRAINT roles_permissions_pkey PRIMARY KEY (role_permissionid);
 P   ALTER TABLE ONLY public.role_permission DROP CONSTRAINT roles_permissions_pkey;
       public            postgres    false    204            W           2606    18200    roles roles_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (roleid);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public            postgres    false    203            U           2606    18216    track track_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.track
    ADD CONSTRAINT track_pkey PRIMARY KEY (trackid);
 :   ALTER TABLE ONLY public.track DROP CONSTRAINT track_pkey;
       public            postgres    false    202            Q           2606    18237    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    200            n           2606    18112    album fk_album_artist    FK CONSTRAINT     |   ALTER TABLE ONLY public.album
    ADD CONSTRAINT fk_album_artist FOREIGN KEY (artistid) REFERENCES public.artist(artistid);
 ?   ALTER TABLE ONLY public.album DROP CONSTRAINT fk_album_artist;
       public          postgres    false    212    2909    210            c           2606    18095    track fk_album_track    FK CONSTRAINT     x   ALTER TABLE ONLY public.track
    ADD CONSTRAINT fk_album_track FOREIGN KEY (albumid) REFERENCES public.album(albumid);
 >   ALTER TABLE ONLY public.track DROP CONSTRAINT fk_album_track;
       public          postgres    false    212    202    2913            j           2606    18102    modify_artist fk_artist_users    FK CONSTRAINT     ?   ALTER TABLE ONLY public.modify_artist
    ADD CONSTRAINT fk_artist_users FOREIGN KEY (artistid) REFERENCES public.artist(artistid);
 G   ALTER TABLE ONLY public.modify_artist DROP CONSTRAINT fk_artist_users;
       public          postgres    false    207    2909    210            g           2606    18201 #   role_permission fk_permissions_role    FK CONSTRAINT     ?   ALTER TABLE ONLY public.role_permission
    ADD CONSTRAINT fk_permissions_role FOREIGN KEY (roleid) REFERENCES public.roles(roleid);
 M   ALTER TABLE ONLY public.role_permission DROP CONSTRAINT fk_permissions_role;
       public          postgres    false    204    2903    203            f           2606    18163 $   role_permission fk_permissions_roles    FK CONSTRAINT     ?   ALTER TABLE ONLY public.role_permission
    ADD CONSTRAINT fk_permissions_roles FOREIGN KEY (permissionid) REFERENCES public.permissions(permissionid);
 N   ALTER TABLE ONLY public.role_permission DROP CONSTRAINT fk_permissions_roles;
       public          postgres    false    2907    209    204            i           2606    18227 #   playlisttrack fk_playlisttrack_play    FK CONSTRAINT     ?   ALTER TABLE ONLY public.playlisttrack
    ADD CONSTRAINT fk_playlisttrack_play FOREIGN KEY (trackid) REFERENCES public.track(trackid);
 M   ALTER TABLE ONLY public.playlisttrack DROP CONSTRAINT fk_playlisttrack_play;
       public          postgres    false    2901    205    202            h           2606    18222 $   playlisttrack fk_playlisttrack_track    FK CONSTRAINT     ?   ALTER TABLE ONLY public.playlisttrack
    ADD CONSTRAINT fk_playlisttrack_track FOREIGN KEY (trackid) REFERENCES public.track(trackid);
 N   ALTER TABLE ONLY public.playlisttrack DROP CONSTRAINT fk_playlisttrack_track;
       public          postgres    false    202    205    2901            d           2606    18107    track fk_track_artist    FK CONSTRAINT     |   ALTER TABLE ONLY public.track
    ADD CONSTRAINT fk_track_artist FOREIGN KEY (artistid) REFERENCES public.artist(artistid);
 ?   ALTER TABLE ONLY public.track DROP CONSTRAINT fk_track_artist;
       public          postgres    false    2909    210    202            e           2606    18145    track fk_track_genre    FK CONSTRAINT     x   ALTER TABLE ONLY public.track
    ADD CONSTRAINT fk_track_genre FOREIGN KEY (genreid) REFERENCES public.genre(genreid);
 >   ALTER TABLE ONLY public.track DROP CONSTRAINT fk_track_genre;
       public          postgres    false    202    2899    201            l           2606    18217    modify_track fk_track_modify    FK CONSTRAINT     ?   ALTER TABLE ONLY public.modify_track
    ADD CONSTRAINT fk_track_modify FOREIGN KEY (trackid) REFERENCES public.track(trackid);
 F   ALTER TABLE ONLY public.modify_track DROP CONSTRAINT fk_track_modify;
       public          postgres    false    202    2901    208            m           2606    18243    modify_track fk_track_user    FK CONSTRAINT     |   ALTER TABLE ONLY public.modify_track
    ADD CONSTRAINT fk_track_user FOREIGN KEY (userid) REFERENCES public.users(userid);
 D   ALTER TABLE ONLY public.modify_track DROP CONSTRAINT fk_track_user;
       public          postgres    false    2897    208    200            k           2606    18238    modify_artist fk_users_artist    FK CONSTRAINT        ALTER TABLE ONLY public.modify_artist
    ADD CONSTRAINT fk_users_artist FOREIGN KEY (userid) REFERENCES public.users(userid);
 G   ALTER TABLE ONLY public.modify_artist DROP CONSTRAINT fk_users_artist;
       public          postgres    false    2897    200    207            b           2606    18206    users fk_users_roles    FK CONSTRAINT     v   ALTER TABLE ONLY public.users
    ADD CONSTRAINT fk_users_roles FOREIGN KEY (roleid) REFERENCES public.roles(roleid);
 >   ALTER TABLE ONLY public.users DROP CONSTRAINT fk_users_roles;
       public          postgres    false    2903    203    200            ?   ?   x?-?]?? ??'??	Vu??K?	??
???0i?ۯA??y?70b?E??t?G?(????w!k.???me?͝ .d????\,?o??Ƕ?ph???.??R?86?W?;??&?xU?87u?\
?Rqi?w?-??66????O???vHq?1*??񄐨.?J?-??Z?;*p??A?R???|?G???N?????S%??jG?3??x????
q?????????Β3?#?刱??????j?      ?   ?   x?%??n?0Eg?+?E??y?3t?????1M?k?_Zyq?xD?qw	???;ϘX?ł)?r??iE??ZE?EWh??o???8?????`?0?1Ӓ??n*??r??~%]1p???P6?????7c???{h?j۟ᇄ5V1??4??X??WXHHa??ݺ7???\????
??W??`'???n?̻??????w?Y???????c?      ?   ?   x?-???0C??Wtb???@;?`daf???I??|=b{??lC??=??AM/?X??^'????-?P?݈-?:K????"zU???#?m??(?;???LE?O???SS?W??ɠ)Æ.?C???0[;E??卝?;;??i?0-? 1;??gT??C??򑟮+ _h<?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?   #   x?3?,)*M%??2?LK?)N%??2?Hw? $<?      ?   y   x?-?K?0D??)8AU???DO??
MId?OC??<ͼ?Fޢ"?Q?u7!???;%Vn????G?????=??IT?G5?H??!??ޝ'?? ><oRN%|HB?0?rL?+?%??N?_?s;*?1u      ?      x?????? ? ?      ?      x?3?4?4?????? ?X      ?   1   x?3?LL????,.)JL?/?2?,.-N.?,??2?̯L?+I?????? &??      ?   ?  x?u?]v?8???Uhs?1??˼[?hY?e?4?լa66_???4xN??p/R?ܺ?R???.?U????d??BTeQ?%???* >2?Ǜ?ث??>?=?ɦ`ƨ????j?????Z??^O&9rP󐬙???????f?UU4??N7??^.V_?:[?p?u?A@#?V?q:&?dT????b?DU?M,?.=Y?A?\2a4???U?ǏV??S?$8=?a ͢?)????_&???L??>\XlV??*???y9q??^=???`?V??c????|?n1?f??2\?8?3?֠G?XFJx n????Q????E??M*?tD??N???Y????,?H$Q/??p??~????j?>?b ,o?I?????Y?ɨCQRPJG?=?7H??JK`?????Z 2?˪???fvV?Q??$????4*+G?JF!I3²?Ȥ??$?hF??+n?j?"
?7J??G??l????C?? `???ǜ"5??pP?%??*? J.1?$?lȌ?7F?c?Eժ!?N[n?q2z^3???mD?-???@?w????l2?A]?9?<??;ǣ?fY??fM#?x?x?????W?nÒ[m?(ѓ?hD?8???$?e??bPh??47?F9?n?'4d?F??d???e????}???8??ޝD?m??j?x?]MԸ??
'DA|q????t??$X??A? ??J`dH?QTa??ce????pU
??`???????P&????!??$I/-?????w9??1:a6R??x???H?ER7Do>IŞ㬅?*sk??9??P???>?0?!'?}!?%7?a??P?I?WԽ?:?83V?TH??{Lź??c???:?`?(ސ???J8? h?x?#?v???@? 0????gz0g??\???h???<??X????HT?f???+7??rИ5
?L?????7R?/?????BXṃ??
zM??Y??<O??͛%?Q?M??Q:??W?ױ?????*?`???4Dj<?e72???3N?D??J????_???;??;??VK??o??Iv6%#?{1??l>Em?W?E܋??X?;\+%zQ?ң'?ٿ???y?l??Iw?R\V?I5????ޟ???+??R??H{?O?-ZS?t5?d?fԼ~҄???6)?i?Sd??&?0????[u?? ???Sڢ?am6/?mF???\ζߦtx2?m?eN????BUDؽ??ʮ?*???fQ?&?'e?????$Q?&,???LF?&K?<3?Y??o1X???O??;?/:^?O?E?????g?n?%?x??&?T????l???;T?J?~q??Wm??'???6ºE??|?y??D?ƁY??jy???w???y?=?B??z? ?7#???????;#?!k??b????l??Ѫ?qY"??W??ټ????(? ???      ?   4   x?3?L?K)J-?442?,?4?2???,?N???9S?2Ss "i??\1z\\\ ???     