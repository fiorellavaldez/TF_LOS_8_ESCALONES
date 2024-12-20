PGDMP      8            
    |            8_escalones    17.0    17.0 )               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            !           1262    33163    8_escalones    DATABASE     �   CREATE DATABASE "8_escalones" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "8_escalones";
                     postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                     postgres    false            "           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                        postgres    false    5            �            1259    33164    escalon_partida    TABLE     |   CREATE TABLE public.escalon_partida (
    nro_escalon integer NOT NULL,
    estado boolean NOT NULL,
    id_tema integer
);
 #   DROP TABLE public.escalon_partida;
       public         heap r       postgres    false    5            �            1259    33167    jugador    TABLE     �   CREATE TABLE public.jugador (
    id_jugador integer NOT NULL,
    nombre_jugador character varying NOT NULL,
    avatar character varying NOT NULL
);
    DROP TABLE public.jugador;
       public         heap r       postgres    false    5            �            1259    33172    jugador_id_jugador_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_id_jugador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.jugador_id_jugador_seq;
       public               postgres    false    218    5            #           0    0    jugador_id_jugador_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.jugador_id_jugador_seq OWNED BY public.jugador.id_jugador;
          public               postgres    false    219            �            1259    33173    jugador_partida    TABLE     �   CREATE TABLE public.jugador_partida (
    id_partida integer NOT NULL,
    id_jugador integer NOT NULL,
    ronda1 integer DEFAULT 0 NOT NULL,
    ronda2 integer DEFAULT 0 NOT NULL
);
 #   DROP TABLE public.jugador_partida;
       public         heap r       postgres    false    5            �            1259    33178    jugador_partida_id_partida_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_partida_id_partida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.jugador_partida_id_partida_seq;
       public               postgres    false    5    220            $           0    0    jugador_partida_id_partida_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;
          public               postgres    false    221            �            1259    33179    pregunta_partida    TABLE     h   CREATE TABLE public.pregunta_partida (
    id_pregunta integer NOT NULL,
    estado boolean NOT NULL
);
 $   DROP TABLE public.pregunta_partida;
       public         heap r       postgres    false    5            �            1259    33237 	   preguntas    TABLE     �  CREATE TABLE public.preguntas (
    id_pregunta integer NOT NULL,
    enunciado_pregunta character varying(255) NOT NULL,
    rta_a character varying(50),
    rta_b character varying(50),
    rta_c character varying(50),
    rta_d character varying(50),
    rta_correcta character varying(50) NOT NULL,
    tipo_pregunta character varying(100),
    estado_pregunta boolean,
    id_tema integer NOT NULL
);
    DROP TABLE public.preguntas;
       public         heap r       postgres    false    5            �            1259    33236    preguntas_id_pregunta_seq    SEQUENCE     �   CREATE SEQUENCE public.preguntas_id_pregunta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.preguntas_id_pregunta_seq;
       public               postgres    false    5    224            %           0    0    preguntas_id_pregunta_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;
          public               postgres    false    223            �            1259    41287    temas    TABLE     �   CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL,
    estado_tema boolean
);
    DROP TABLE public.temas;
       public         heap r       postgres    false    5            �            1259    41286    temas_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.temas_id_tema_seq;
       public               postgres    false    226    5            &           0    0    temas_id_tema_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;
          public               postgres    false    225            n           2604    33192    jugador id_jugador    DEFAULT     x   ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);
 A   ALTER TABLE public.jugador ALTER COLUMN id_jugador DROP DEFAULT;
       public               postgres    false    219    218            o           2604    33193    jugador_partida id_partida    DEFAULT     �   ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);
 I   ALTER TABLE public.jugador_partida ALTER COLUMN id_partida DROP DEFAULT;
       public               postgres    false    221    220            r           2604    33240    preguntas id_pregunta    DEFAULT     ~   ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);
 D   ALTER TABLE public.preguntas ALTER COLUMN id_pregunta DROP DEFAULT;
       public               postgres    false    223    224    224            s           2604    41290    temas id_tema    DEFAULT     n   ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);
 <   ALTER TABLE public.temas ALTER COLUMN id_tema DROP DEFAULT;
       public               postgres    false    226    225    226                      0    33164    escalon_partida 
   TABLE DATA           G   COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
    public               postgres    false    217   %/                 0    33167    jugador 
   TABLE DATA           E   COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
    public               postgres    false    218   [/                 0    33173    jugador_partida 
   TABLE DATA           Q   COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
    public               postgres    false    220   �0                 0    33179    pregunta_partida 
   TABLE DATA           ?   COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
    public               postgres    false    222   �0                 0    33237 	   preguntas 
   TABLE DATA           �   COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
    public               postgres    false    224   �0                 0    41287    temas 
   TABLE DATA           B   COPY public.temas (id_tema, nombre_tema, estado_tema) FROM stdin;
    public               postgres    false    226   �Z       '           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);
          public               postgres    false    219            (           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public               postgres    false    221            )           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 281, true);
          public               postgres    false    223            *           0    0    temas_id_tema_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.temas_id_tema_seq', 11, true);
          public               postgres    false    225            u           2606    33197 $   escalon_partida escalon_partida_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.escalon_partida
    ADD CONSTRAINT escalon_partida_pkey PRIMARY KEY (nro_escalon);
 N   ALTER TABLE ONLY public.escalon_partida DROP CONSTRAINT escalon_partida_pkey;
       public                 postgres    false    217            y           2606    33199 $   jugador_partida jugador_partida_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT jugador_partida_pkey PRIMARY KEY (id_partida);
 N   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT jugador_partida_pkey;
       public                 postgres    false    220            w           2606    33201    jugador jugador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id_jugador);
 >   ALTER TABLE ONLY public.jugador DROP CONSTRAINT jugador_pkey;
       public                 postgres    false    218            {           2606    33203 &   pregunta_partida pregunta_partida_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.pregunta_partida
    ADD CONSTRAINT pregunta_partida_pkey PRIMARY KEY (id_pregunta);
 P   ALTER TABLE ONLY public.pregunta_partida DROP CONSTRAINT pregunta_partida_pkey;
       public                 postgres    false    222            }           2606    33244    preguntas preguntas_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);
 B   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT preguntas_pkey;
       public                 postgres    false    224                       2606    41292    temas temas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);
 :   ALTER TABLE ONLY public.temas DROP CONSTRAINT temas_pkey;
       public                 postgres    false    226            �           2606    33208    jugador_partida fk_id_jugador    FK CONSTRAINT     �   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT fk_id_jugador FOREIGN KEY (id_jugador) REFERENCES public.jugador(id_jugador) NOT VALID;
 G   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT fk_id_jugador;
       public               postgres    false    218    4727    220               &   x�3�L���2�P��B�B(3e�, T� r��         7  x�U�Kr�0���)zȃGY�0,�0â�nTl��cg�6]�"=k����?��~I��X	7*�)O�g�]��a�5jdD`G"xQ�JFPud降K�
�zK��*�%R�>�
��҆�L�Hwl{<UZpz�e����,��`�h-�F3vm�:�p���|� o��Gp�9no��vV�b�� �xW'�(d�Eۄl�����@�������M'|ş�����!e��Ғ�o`۔,K���C8�2�%���+H��S�U[����0�)^�ѣh�����4���|�I��)1�Rc�y���ݘ            x������ � �            x������ � �            x��}�r�F��5�)0���Y\nQ�&���T%�dQU;�&	$ɔ $��UT�M?�<�/�.:|�8'�����e&�$(���m��\����L�����e�/��K(��ᤖa"�;9�I��oYx^�,��8
���q�������
��0�I��51C�$���k��e�2ő8�m�RY��M-����X��(&2���.�B��u6-�_E`f�wu���l���Z-�d�,�B�9��Y�	�_��\n�����`X�/*��2���J�e������a��(e8QEj���R�#KB�2<++���L�i����4:���l�ecpK��!�\��j��"lȀ�AC7Qpꑜ�T�tk�s�M�/�$S��F��vl=�5��2��	|i#`��=8����h���e���16Qh�A�Q-2l+ҩ̞,#�����	H��R��Fd�GY���tp�*�(��h���PcMUVd񗎔�N�W-��)D��牚�[�I�D'�(2�
#��F�p��}���������d���[�n��>|��DS��'���nA^�����Ȝ,�Ʋ0���s�*�[s�����`�S���b&�{ Cf*x+>�A��$�����gb*�p���,��(Ó>��Rvl���6�H0	�%��ވ\'��;֙�W�(8vŪ�ЉH���R�e����z%U�����?�upڬhMc�Te��k\"�!ƃ��M����n�×�����9�,J�IBM�r��6b4�����!�S����!�p&���݂��h����XC��jX�`�Y��W��5E�d�B:3&(72�o����B��*��T�5�Q�C*�!t�p����qr�I�:9� QFҊ�H1�.-�)�Zr� �UFΒn��2Y~	���(��,UpB�Ku� I�)�1����������!8�*t�a�-+��_9�w�_x��DvO�XDpn��L���L�)v�)�ni���Uq��Ɨ[���M�R�sJ?@.�n����^�z�(�CQ%�R%L�!)�]H��5�;��a*+�6��^�����v�=_������DR��[s�c��^��n��N����~_覂*5,�07
(k'uϐ�J�O���[��׍}�X���y!�
>��s#b���L1������2��u��1��9�&8|�͐֩1����TN��U�����x��3[��WT����մx���KSQFu�I��72G	-�%�^˷���o1���4g�1�s���"QO���������[&-�<�:� ,o��M�߬�U�8e����v��q��
�x;K*c��2�n���Vь�s;�I^�����.r	�W<�����n��W:�U��֮OvX�4��3��!:�H�T�]��?jZ���xA�rx\fӄ�����[��J4�uvr{�[n��XZ{+�30FdD8�eRy���
��3$��K��<cR�;��*�얮a��+E�Q��Y3�@Wo����
n�8��-�U��$5��! ��ۯv6=*F��IF ���LX�\4n�J����pL�cHV\i`��c�A���zȒ,;�H�Ms �U�o�Tӗ�,w$���S��Y� )ft8�W���Ű�o��%�~�� KXl�=��e0f��i�=�������ʓQ]���v��-�s΁x�ٓ4D����B*��_���VG�s�u��yս��^]v��|"R]ꆨ�f��`>�D�{�x�p{MV�b����J	��
�_�D��N0v�+�DE� �	[�H�T"B���(�����D.��Q��Q%���)��9i�^�BS��c��H䘐��ˎ���"z,a��%:zD����D���i���	$ �!A@��a+l�/�uy��e'���

��$SPl��W%��'�>��cd�8���t��Þ��5�ə��t����X�h ^�:e�i����?<1!N�\�x>�oC��h�,̼Ssi�j��ou�՜ ș��/�����;�5e��SF��exS 8��g�ˤ]�fVv߈zZ�,��Y� s!:�V����`M�c�	�DPV��T�I�`��.R��x�1A��)\B�B"��h��x7gg�0*�r��w�&���.��{e�Qҍu:��ɾ�7z����:3��L�Z����t�^�)X�ز�m���+�X�ұx�<���Ϩb�	G[~Y�EO����2g��s�V����C��Z.W��6���n��8�0N�n0���P�}�~�aJ��F��6%�����z�)�鸐6��j
I����z�u��yS	<Ό^ZK���fz� >#`b>ɨ��:����U#�~�ͦ�l�X3�E"�I>�Ej��a#:��*k��B�^�~p00�::葄`�z کE��(��T<� ��O"�V0)0�%��+'j;�v�@�A�d�҇41�O��c��H6d`9L�_
�����}$�}mX��jo3��@�b��.~�5��"���X��A�� �cD�c�'͐�)�R� ���	�Nf]<܋�ځ�|���f����3���	�k!N]���u;�BH���L�gj2�~J��2����8m�y����f2R?*�/ţ@�	U���v=�V0�/�1�guA�I��d��x"���$L�����~���+��s�z���w5��ߤ w\Ң���j6��<��0�kr�M!�uR��!NM:"�Ո���A\^�X1��LHm�����Djl�7�Z�?�B�>φ��������W!�`��D܋�Ɉƨ��Z��Y�c1�e���o����#��D����
�W��$���1�'�h��?�C�u!�'�1�G������gS�38(����zk���"K|�Tb��0gX�x�n�<��z�{�:z��c����=���p+F�JI��ThhD�f�$V q}&�[���<'�fU&��d��4�3�餣����s��D�� Y,��N0�����{�������d���W��> Ω��8k�V`�)]t&n���I%��2�>,ϩ/�'�H����W�=��,L%�b�[����AiX��8�=�?/�Ij�%��aғH1��SM@�9Z(_�,T(fFc(�d���	�N�_'���2ԕ9@����W�=I������-%���{.�XN��U�E��A"o�-��Zl�IV1�-���T:A ǚ/��$�(��s����)��g��D1�'����b�(�o���8�mF�D�)�(�[�L���@���v��5�<�n��]����@��_+Tp/��<���z'6���+���m�O���W!�q�3����Y��T�,8SN��%4
U|RY���3vRɌ��j8$�?��e��Y�Q�i���Z0� ҄=Ԕ���t7���D*�6��M��Yd�~\G6��C3rGL=e��L8��/�_!�wF0\��,��l��9S��$1��m��n��Bu�@C0�,�Qe*�7��/nm�ַ��y�rjͻJ�#k��#H,zEc|�ZYD5�Q�v��Te<ׅ�=�T�F���2V���X�%�G�ʵ��G4ᦸ���[��=>x��)��?nWԇ�� ��Q����	�q����s���Mhxt�Ҟ5��˔�,��Q�AN��Y�MMj����n��B6'�2�mi�(lJ�4ڢ��"���i&a B A1!��� ����Ý)�If���b�PU���[�	�ŋ��b�[�ZU�$ʨMz�Q�~�v�o������$��07�!��IS/4潐��TAyF ��)R����)��r����h�^��a�6�w�]=�H��0�i�����4�&�-��h������)ye��-s�,�.�a�j~�sa~��ǃ�v��L�f�-cN�F�@ vA�ބ���a��%�~	���le��@}aJ>f�.ߛ�obA���8I̗P�B�GxX�xH$���N��
hc�'ZT��� I̱����.�P��c���c_B�b�E#�����N̠p��k��i�=�=�h    p���:�a;�Jy���g�I��ul�kJ�ָ�i��N�����w̔[�r���4��ߕ�l\)���?`S��	j)dǴo�tQ���5��`viksk����v��
Ȣ����Fc^�?�qhŴ�� �����[}g�	�L�X�� �6
r[K�m������mq�$o���m�6��~���ve#���

�i���f��|�	��zxu<����67�	}=��iJf]�4�ǎiw5h�
�Φ�<h���efʩ������Ý������
sY�LL��c����,��\5>���w&\l3
�������zz�*���c�K�	�lCR� V��f@�؛`�����"+�/�F�4;͜!N�Kk.`��a����������6�yTcY�:�+�n}=!�;l�O�J5�����8���T=�8|�����H'���������~9��|_Wy���liF���$������ɝ����
�E����G�^�ct%�c9Q�q��9
�4�_�����9og��w� $7ܴR�����?�XI��J&�����\�����%�y�}L����)J�@�a7r!��6�^���T��\'�]��,������c��^f"�OL�S.��f�'��oe���ϐ�Mlp+���9��T���������-I��}���Fʀ�P����d��E�(����$��9{@�G�~R�� �9'���hlw]�ԕ�9����#�nmiZxSP'N�3�6��B;���(#UW�^��6f�'�����v6���1o$l���C�O�YSF+���7��T{�.�}y,�'�IJ�4Ь$�Λ�4OL����B�(GM i�-�0<.P�4�!P!�R.���_�)�1׺<q�xG�8�Ӵ.Y�{�|޸�kI=h���v�Yϟ�(甈K�r��\������H�
At�<!��^9���}�%<
�(00ڤ��)i�
�Xoj�_�@��Ү�Nk&�r��H"=[�f��)V��L"�-5��
|��ݴ�h��$.�s.�Xv�RA`�;�y��g|��E�Dun=�h	ב\�Gi`L>4��a.�ٴ�-�w&�QѨM�����n6�#���f�,ӜΘmlO5�zh�i�Z�T;3ͅg6���F�Ĕ��t��
�R{DNjۀ��p��_��X;Vq�t��w�g��{0��Ү��,���Wwe[c�l��a���bD�Fy�� �)����f����L��&h�����0g)T���l��04o�;$�_+�y���'ڍ�V�.GiDM?���X�r)����L�Ro�5R��ؔ�����i⚱�PLᏄk�c>� ��Ѷ�p�6w�r�lp�J����Q>�8��F]_2!��k�G�!.�4�3�am��(������o��9�_���u������V��1�6.�E���K�9T	l�Y�aD*��d�5R���Y��&��ip_��[�γ�.�)D���o��>�6����x>)�pq	~�U�h_��q"��kx*�������D���q#������G�E�y$�cb��BJ��ՒV 0��WJn�~�K��VN����� ��-���1�\S�>?�cϘ<4L��oN��|Ik���]S�&�G�������O
��?=:�C���3vn�g�
O%O��Qx���k�/�)���ȸ�NaI³��9/V�}y `eDԧ���g��W���Eg���-����	�ds4�K�Ⱥ�1�~�v��)<�#�+4Z@�>�q�����>��v/y$Ž���v��d�A��,-Ȯw���$���fk��$�֊00��*����
ގ����]�2xV�R����ǒ9ϊq#"�ih�L���=����^`���[����ē0]���3|3���G.w�E3�T�^ض��E:�aS<�2����Ix�Xΐ�f�i�9�a�jە1�M�hz�lP# sF8�1��!CҊMsָ�Ov�|.]����έ:���w�V�guY[#�&I`�\�۸m{���	�ϡ ��dBwp�;w�0J��%N�WGh@���l���t�	#�I����]�d�
��rz����.��$�����+KKt$�O�e���V�p�*�J	�]�3��5�Z$�;`V� "�^H� �9���k��S�����IW:t��3���ib&���j�l6�dD�t@S�����d~Z�q��܆zЋ	V1���GŰ�����e����Y:W���R���b�L�&j�)sK�`���5In��p�v���[�D1�H;rs�±�VӦ!��;.�X���l1�ύ=�# $G�[=�^������A��<�2YxZ ��4�޾���8��ޜ�v�v-	��y�4�Տ�/)uz� mk�c�9�"�4����~;��Ze2*Ĥb���qp�x%|#R�=E�#��2�0V��T��]9�徉
ZF��B��4+H�,|b�E7��cխzѬ�_<s"ԕ�L��d;1�H�J�H'*G�djhI�q�}��(8W��5���sS{V���2��;pOL
s:)�l�3ga2�k�8��H5ۣO*�it���u\,�:��)S^���êf�nC�Up�&_6{*��B0��t����Йu��C�M��VD�#�:{���@�r��K��fR�^V�*�����؋UvX�u@֟�Lm.9�1��M�̦����Ұ,E	l�����	���J�\'�!g嘆��e���CƐ`�hU��xN
�� {�����������b�h�2��@�
�[�q��EXզ�C	��#�]�)�H����|� !&
�v?	VG��wz���m���t�פ0ٷ�(�x�$�F�F�ن���x�~8~�.��\:�����~_��,z�+�Ԧ�M�w܃�^�I���(գ���8���o�#�`C�n	{�T0']r������� ��e�
$��eD��	D�&[q*�ҳO�"�	a�)c�gs��щ�/�s���T�N�ox+�_�'!��	]	k82����u�J�"���'8_����?կߨ��g��.Ac>/j�'������"��-�����g��+��h:�q���r,�3O�-`�'�}q���0�MPD�4���ωIlo+��v���	dP�~,B���g���m����Q%���Y�s��ca�������<��k���%��	*�3Wt*>u�ak��ΰ#������A�r+n�*]f�>�h[��>
����1�3���>w�����No϶b��aMs��<����3��Z��ï�;�:�~��T�3�[�߇�Y��t��:m.A(k�a�����s�ϭd�]�w��s=;wpV��;�H�]ށ�<�� ���0����Tw҅)�8al�T:֟T�:��}��W�:��9�G��ĚM�IwD��X�6��u؟�h�'D�h^k�����8<O�"�_����x�:�����|�XǋiͳM��g��@�D�U[�ڻ����q�*�>�Q42nc�i�}x+s��^���`p��
>8���1F۰�v,y��4�It�OFՀ�'��+Cw0��V������Ȟ`�x���e�V�w2�*`�C���qp�P�OZ��[�ejb,^l�k�֞'�T� ʹ��Ni����њԬ��-u�]����$mFJ�o5�b��O��OlLa:^���	Q/�|����X��� t�`�9`��a��-v������b LPpA!�)�u͞��m�}7UW�ny���j��.�q��G?�b�2�ѡ/�'(
�-��63r=�y��ڙ�F2�����>O���3O�^�t��"v]E�>��L��7 �D^B�� +߾�xfϋ����M۞�����L�ʺ�L��nΞO����q`�"����w�^7]x3����+^����"S�ޟ�)�|� j��Az#kôFL`�9���MAT
=�� \"񖰻Bu�A맵��]��|��~FH,yB�~�J�|�M��6�i�K�Xq%Ʉj�M�nl�ekkwù��#h�DDvxҌ>) �c��,a��<o�f��n�P�M�sD�x;J%��Ѡ{I'�+���_+�D���%�N����x@1f �	  \����5� �⭣59���U�3��Y����ǔus6,RX)�{��#�e���*�yR��2x� ����	��תN���1wTi<�e/�d]���Ơ��w5^��V����KS���
(�f���c�e{
i��H�� �e��E�[��[i�rw�-���O��w��Q������&�;�y�cs}��Rຠ6�b��V��K��`��d�Ǭ���e�& Sbr��w+�c��iE�L�Y"'F�����Gx*%>��oo��ӑ����h5��l�������$���l)�h��;���ͮ��f<_�c<0��Ӱ�n�˓�?��U'9��m�d���F���(�q�:�W���T�3W��=�~4��aqQ���c���m�I�'7i�_�t�K"�:X�uZ+6$A×���荠���p�[u[Hyv2n�n +?f?��(@�qu�ェr��ا�N��Q3]��o�)����Z3�ݫi!y�[��Ⱥi�B��3ȍg�k�����ְ*�Ql�As0Ӵj��"�)��
���Ӯ�Qj��ɧ��D'�1���(�_��w @͙,p!Jm^N��֌��O�/!���x�Y���Yŭ��WS[��	� ��Vh�(�)�S0��~G�;:)o	k��K� �Kt�%O<�=�D�W�������]kQ'�9��n�{b�k�n>83�L����[D����	Ȣ�	����H�ce�A�&2�- "�-W�<*#s+����x��q��dߋXt�������E?���D����K���84�b�����Vӿ����?��u��i
�[a��p�ڌ�2a���b�kH 9m�Y��?��4����=op��h�ۭ80�֙[q����!�MP��[s��B�*��n"Nܵ�L6j'M�,�)��x�Z^4!���Լ"�aΉ�C�������K����M�i�����mI�i�'8K���$ɻ+{���`S�����=��	�N����!��X+$�Nk�)��0A|�S� P6�iv|�b�`�����_F`PE(���������,/��i"3לm��H�Y� o� o4�2,��PC^�����Sj��`���;Bc�[�,N�F��ϕ��ް'��q#s)K�EY������B�d�<Nf��Q�3�����ܣY���i�)$.�N^^Ε��wp�wȋ��+6��:��Y,$[Մ��̐�,n㞧T�Q�!�᭪��R�Su�)��X�[�^3���)й?�Jxa��������Ϻ�屡-6�l ��f����� c o�f��7��x��2�y��cմfq]{}��edx5�V�Rm ���:��*���x)�;m�H�'2{�uh���`�jS������A"��m�c��Rhi o^ft�&[�LO@X]�����O��P3��W�eKV8��C?��2�Ih��X�0o��x<5)�B24�x�/x��ۙ6�r#67�ctR�(���:�z݁��r�ʽ�Ԅ�����lBT���՜�Mar���ҾtD��� � �h�k/�%}�c@�8���27ȑ,oY�)U�c!��Z � �.��A������G]$q���[q��?�%`�̝!y�2~H�\0�f#�̈͠�É�C��\����s��s�JU��N�`������`���ih9�ޥ��i�7��3�W�]�B�-~O��s|��������iϸ����G3���ab �)SF�y��}2|�x6�a{���#`�m&2�J��P�G|H�h	0]8z�g���pվ�5�'�8h�o2��_�Π���i�v�^��	 
\ǝ_�\b6�i^#�L�Op�3ow���2�\K�:�	����k���ִ�����~��ExS�lؙiN̞����Jk���X��m�d��{��Ec�9ڋ=�3�ʝ�2�����0's���t�I��� 3�zZ����U�S��h� �2{n`�F��Y��B����WlZ�oSs$ ˂��P؎=3����.�֝��<� �Ly/���g<o"<�	5��I���44���ry̎s���9
4o�f�bv�����\�o=��58��������W[��E�[�m�7QS�=��#���ڪ͕����cN�n�� :��X��+6w�_U{a�h�"�y٢��b@1R��=,�#������x��%��cC��������ޏ_�5鏨f���`���:��u2����7�y#G��Z����dd.�|�������D���4��Lí]�,�h�+���]��;6�qs��\W�����`�'�ч��ሮU�7��h ��a!|�'�[H�Ú-9NTo��`����9��SO����7k<V��w�"-LE��y��^������'��cQ۴�����_t	פ����pݒ���Hq-����2�j�E2�;!��:xs�;�7�K�`�ߊ
^��-r�x)׼�ߚ���˵�+���"ouU1���"�BV�"�J�c��|��ի����|         }   x�%���0��� ̛2)4H��hN��>���c�nfg-n��F!d����3W�b��#���/{\���|�[��DC�)�A}?�������ĵd��xZ�k1�"�,���2�� 7�.d     