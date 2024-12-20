PGDMP                  
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
       public               postgres    false    220    5            $           0    0    jugador_partida_id_partida_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;
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
       public               postgres    false    226    5            %           0    0    preguntas_id_pregunta_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;
          public               postgres    false    225            �            1259    33188    temas    TABLE     �   CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL,
    estado_tema boolean
);
    DROP TABLE public.temas;
       public         heap r       postgres    false    5            �            1259    33191    temas_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.temas_id_tema_seq;
       public               postgres    false    5    223            &           0    0    temas_id_tema_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;
          public               postgres    false    224            n           2604    33192    jugador id_jugador    DEFAULT     x   ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);
 A   ALTER TABLE public.jugador ALTER COLUMN id_jugador DROP DEFAULT;
       public               postgres    false    219    218            o           2604    33193    jugador_partida id_partida    DEFAULT     �   ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);
 I   ALTER TABLE public.jugador_partida ALTER COLUMN id_partida DROP DEFAULT;
       public               postgres    false    221    220            s           2604    33240    preguntas id_pregunta    DEFAULT     ~   ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);
 D   ALTER TABLE public.preguntas ALTER COLUMN id_pregunta DROP DEFAULT;
       public               postgres    false    226    225    226            r           2604    33195    temas id_tema    DEFAULT     n   ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);
 <   ALTER TABLE public.temas ALTER COLUMN id_tema DROP DEFAULT;
       public               postgres    false    224    223                      0    33164    escalon_partida 
   TABLE DATA           G   COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
    public               postgres    false    217   /                 0    33167    jugador 
   TABLE DATA           E   COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
    public               postgres    false    218   S/                 0    33173    jugador_partida 
   TABLE DATA           Q   COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
    public               postgres    false    220   �0                 0    33179    pregunta_partida 
   TABLE DATA           ?   COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
    public               postgres    false    222   �0                 0    33237 	   preguntas 
   TABLE DATA           �   COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
    public               postgres    false    226   �0                 0    33188    temas 
   TABLE DATA           B   COPY public.temas (id_tema, nombre_tema, estado_tema) FROM stdin;
    public               postgres    false    223   	L       '           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);
          public               postgres    false    219            (           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public               postgres    false    221            )           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 152, true);
          public               postgres    false    225            *           0    0    temas_id_tema_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.temas_id_tema_seq', 33, true);
          public               postgres    false    224            u           2606    33197 $   escalon_partida escalon_partida_pkey 
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
       public                 postgres    false    222                       2606    33244    preguntas preguntas_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);
 B   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT preguntas_pkey;
       public                 postgres    false    226            }           2606    33207    temas temas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);
 :   ALTER TABLE ONLY public.temas DROP CONSTRAINT temas_pkey;
       public                 postgres    false    223            �           2606    33208    jugador_partida fk_id_jugador    FK CONSTRAINT     �   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT fk_id_jugador FOREIGN KEY (id_jugador) REFERENCES public.jugador(id_jugador) NOT VALID;
 G   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT fk_id_jugador;
       public               postgres    false    218    4727    220               &   x�3�L���2�P��B�B(3e�, T� r��         7  x�U�Kr�0���)zȃGY�0,�0â�nTl��cg�6]�"=k����?��~I��X	7*�)O�g�]��a�5jdD`G"xQ�JFPud降K�
�zK��*�%R�>�
��҆�L�Hwl{<UZpz�e����,��`�h-�F3vm�:�p���|� o��Gp�9no��vV�b�� �xW'�(d�Eۄl�����@�������M'|ş�����!e��Ғ�o`۔,K���C8�2�%���+H��S�U[����0�)^�ѣh�����4���|�I��)1�Rc�y���ݘ            x������ � �            x������ � �            x��[�r�H�]�������W�z+bzzٖ�W��]]ћ$�$S��@�����Gx��y3��s2�"(���\����sϽy9����i�[�����M�D���/A,����i$����V�x�e| ���|���ր/��H\�B�m`��K����R*2�e�G�:Ri��H�ɃӼ���I5��Ñ�S�:M����؉
��|��IaRq75�̃s5+��ƹ���a$��Y��ʎ���B.Kk8�����s�}�q{�|�f��f��G��Y�Q��'�Cy ��΋ŗ���c/��╲��c���X|����i䦼��2U���0�[�ge��8����n���x�/�LC�c�]�{���ź���`#���q����cd�Ts$�{�����X%2�R�ya�|��L'v�Y
7;>�-s�ֳ������q���@̡��ځ��eA)z�*�,.�o��31\|	�,p���^_�
��&~��&�]Tb��EvwwjAQF{�f��+�
��`����}d�p�f��Si�v ���5lҚ"�����k[�|���`�̓=x��f2�
��ؠ�6>��z�����J�1������	lR\[�I����#�\Ob'�̚��7}�:K#�m���[�;��gx=�E��#n<��F*SXQ�[����ۃ������+*PI�� OOἥs�.*�Լ-�Z��u�́�R�6Fϒ�Qjĝ.�b�=�4�٪u��Ʊ�kxgB��3��E#��~q��X�t��fA,�q3
��:�ys;�����7o~O{Z=�VE*�v�+XЕ@Wo0F��>��"���cs3�η-�hf:�X�é�J��Vy�{ _��"������=n��w���GS`\�S1,GS ��c�G&W��w;{ɂ���%�����Jf&V�ޑI%�P�z��B�2�H۽I����{�B��QO���I>gLk�+P��zi�h���a��]��&_������[�7����ð&7��U�j��h.��W@���}9�k�<��9���@37�x� P��#ب@h�����5��`D\kR��>L�� �?�0�$C�ʃ�@5�s�}:�>|z��_ߪ��tB�r�f�Bc#.0Y|̃	��s����Xggq��/>�mRZ��s�c-�9��9�4��FDUbE*�}v�?,�Xq����x�
	��q���\�&$�9!^�ň;`z.^�x�N�ՙ�Cz#�:2e��s��`��X�u��J�U4�va�i��y���ʛ�,bU��D
�b�kqEybk}=HTՊ��rй�n���w������LƊF�0��.����!6Ŗ�n�a�otI�:�K�eMW�E'�%��m�e�{�F�Z˙�a�(D6�t�d��0�	&x�`��xez��rW����v����k�8X��ݭ�*�t1O,G�&Z�TF��Ll<�\r�\]�&�i����e�I��KØH�E���ms��#Fw�b��1�P=��y�' ��H���5n7Jt�����A��\|��2��^k���t��	�����@��V ��Y1䁩-��KNi;7Sg�8�5!尙B���0cp�����	��j���;�/���T���NjU.Ӭz�_���r2�U��Y:��lK��e�(7�����n�� AV��(�g22��*.ȼ�}�� �f{�A�' e�)B��M�%8 ���wv]\�P���ҹD(@�H>�)$@�w1 $
Z�@�P�9!���s#�cY2OC�)*�l>�Z�8�%L�k9*I���O0O�.L9��)�`�������Hsqa@����� ��Y��%�L
��ಟ��ǒaqi�CϜ=�H��8L�9h��2va^��Ӹ�,1�F���H��,���٨�7�B#���EO�Y�Rx�t���-�������n�� 3�g�o��1w�'0�`�{:Q���=�������8k���I:?���M-TF���#��w��b+��ep�T*��K��O�2MUk�����C�l��ˀ|�"G�V��у8/����D.��H�aV���vE�;��z���n�7w9"�,����޹r@"r�؄�H0�,x���+���h�5� `$ȍV=lI�eqd
؛�.[�l�94f�+5�)i6H�-��g�])�� ��G�&�v/�=[IJB#ř����㐴�y1�W�I��~=�=DF$	� ĐÉ�����Ȇ�4Q�3�[=S�[=79VsN�6~m�cg����H&KڶO͜Y����"�����d���v_�rRjV�R���a:�Ŗ����`Ū#�	UY7���m��2WV��cc��y��1�A>�	�#�w�� �����F�xH���E&��������8f,s��^�u䌈���8�7��϶7W�p�ȡQY���
&�)����ij|����H�caKG��䭂�z���}���Ve�s� �2�����ڽ����!� �1�k���5����M�.��փ5f�4Z}׼���R#����e�#ܼ4sي|��R����y�wSXR䫷�f�u�L����\R*r���y�f� �#�bi�.;#��0����F�.oZ>�T�,<��6��Q�`}�w"����M40��Jγb;K�1����c8h�'�A��'�qT��J3�'� ����tR R �9��tej[϶�9���ɥOi"�����c�*Dv��.���c��:T��>ת�z��.�y+H�g�E�_|�R5�*�����y=B�?��S9��;�/'0R]a�y��f�Z�R�f��.i7p3�?f� kg���U{R��L�^ŉ%Ab�wg*8�����
G�k\��x��"��@�ֆuM󠍸��D
W���w�;Q5�`� W�OKKܤN\)��x,ᑇq�#
�4o�+�i��wR��&���(�I�r����&Vک��Dw�K�>}��S�ᑡ6^Z����)o�
��F�T߰�x���4s(؄2�έ�����K]��-;�y�b��+��k|�p~ E*ZĝL�iKخw�_u2��R5{���kUV � X�4��C��.
�^���1�'�6���C��R�O%&#�!���J�/��O':cr�[����7zk�֩"/|rI�N0�X`\��p7�#�^X}v��i�8�g��:�PU��@�B+f�)\lh� ���,V�q���|d��n=e�n��,�.�i�����I���F����+�$�L���b�oM�	���n�gX@�(꩎tx9����aZ��0�D3�)H����M
%ު�D�����_ O������v�z�ϙX�C�MBn�t����BL�Y:����&i K< ��<&���U2��/��\(�nF�~RRB��U'��c��ӱv�UHme�����{
R��WJ�'B��D���4��n�W� �q�nV?�����5�z�m�x�k��<�7w���8���3d��#��<�tT_� u?T��Pڑ�hb���/��	��>
��-�8-}q��X����1�r�-�G���A"��i���(�a�*�M$D���%��=ˤ�~�p����1��9�6�����A��
d؀��ɀ� ߳O�TW~~��p(�^������Z%��#�� X���m"�g��!ZNJɜDȐ�0Q�^�0�+�9�ʛ$d6v��g1�qg��OcМݑSOX��^ ��ϰ?���3��b}v�6k�S��1��޹��,?�+�\C�P�i����^��_�X�N�o����hj%�*�#�jP�3$��Ec|`��a	��ݦY�w]7G�u�绮\��~?PF�V�7�T���m	�!ܝSiօ�`c���{O�u�)����),�I\�E�������C�ը��?��OcB���Ωܓ���JUr�0�-\{K�A�G]�P8�=�|��7�s&O�*{W)(�lN���&JC�-�:0)��LR<�	AvL�����6����(Y�f�g��⧐pU�����8���ǯ�ڕ�������w�~������;y+�����IFlݤr��Pr� |e<�X���E��e�*�V�    �l��e���fV1��0c�뽛�F۪<W�s�S*�#��2q�t�]G�1	Yx�|�(@��ؖ�9�����N@0�D�d:b����V��R*��fc�;$'�%�K���$�Չ�X��+��?����uz�{�������L���v��F����Y���σ!�3Ge�r9��J�7S�W��C�װ��׵cc}I�^��&��t�=?�e�a�`�tu�ؐ��X�bamʳj�M���,~.�igp�ϋ�5��>,t��ڍ��Y�A8n�}�*���# I+�%xgl����ݪ:e�n�so�BЮ��s����#�`��rg��&�C���] �5�g�ȵO�;��y�3]|�F��+�Z֭�,��ļO�<8�?�q��A���2<f��޺� �c����n=�CZ"���v yJ����³L8���gP�����U��3_� ా�T͔.������-���h�R����Exxe�.��̲D��W��< �%����~��9&h�!���U�U��3=S��^����佩Rd,#3�D��D �KS¼��I�@�����1X�[��H�>�ُ˹��sE!Uy$u������+��rf�Y���l������9�EQ]���Y��Ic�>}N}��MD�r`c5/�yT�;�(�3����z���y�To҇�+NL�SB{H^��Q����C��A�~�W�T�G�˚s��sI�K���(��=�5�H�qƐ�N��y��N��+g��&U��o:WVb1����~�L�n�,RΡ��>0X��1߼�)bP8E(��6�0�� �0�+�{o�q5�	s��x�:2�&�g'�$Ho�^���<`���.7V���NtNPaMݹ�t=�;�5D;�;�`��LF��v��\(G��}�t�i8���шV_S5���
�*���ź�K@M`���Ԓ0���"�����"D���3��[�i+խ'�BM��U͆KbXkpe�����n`M�K.8��b���N*��Z�ז���7׾���Kh;gc�,V�s7�J~���(d� i��a��I]@\=g��
�9��/x�F���p���ľ���H�כy1e���I�2t���?T(��v)N�L�s85.+����gY|���a�Hz�;��s�"A����a��o;s���͑t�-6�͔��O&0`'1O�����p.�"6����ua�s4���I�I����JoI�H+@k����:s� �
�����ztr��ڟ�F��_N8�uYd��g!���%�-����U�F�:�<�c�Ðד����YY��:uV�*�@��;u� q^s�V-���%O��b�*�������h�d>�� �T{�j��рL�[����E�&^�;&o7} � ~�I�����?�����σ������>������V �}SEHt7"�VU�����D2��=��� Db]���)�k�:�z2��ܦ��j�>�\|M�A��4@L�����R0;%3�ݶ 3��\xyT�F ��R�W�7��n�W����ɋ�׎L�d�܏�;�T� �e�� 0��#�P�-��3�U�X����('͐2u+{���ii>}�}�4�������?���D�ț5�+Vz ~������?w䴷��g'���+��.'�?�Ȩ��4�iD ^�&�F�GF�dBp� |�l�?�� v,���(N�F�_m׶��c)�v@��mB�����]�uw��R�30�)L^;<���?��p��p�i���ʸ�.��^}���fV�
Sx�5G��':=�
_h/^M�&Y��(B;��B�������+�.���+�(�S׃GqddA,�KF�k&9�R�t���*��W��V�D��x|N�Q������X�yF��4$+��V��׋���Qv�4* ��\��< M*<�13�ܥi� �5��hjċ��2�e�I�i<��'�e�����E5�-S�}���6E��*3�K=[m c�ȣb�Hx,'�#WXn��- (| �m��U����n�����-K��6k�D�a��Ž�N�󝐇�X��#d�3�)��1��|�$��Wo��2V,~���2���du����K�7��tc_7$4��#>HXyF a/�TE0Z"2q.���3��Iu$�?]�%��W�1IV��t���P�;�+�,�ڰ?��=��3��DU��ѝ3����C]���\�g�!�$m�kd;��Z��j�HY���������� �V�X�I;��'��>�qu?��G��ZJ�}Z�$4կ�t�Ů�`j' ^���D�q�U���V�\�|V��-�x ^ZV�m+̕�ӎ9.e�1���2g����e�\�/������_r��vV10KA����S>�U�4����u���Ԭ��l�k���\u�ӕ^�3L��ˉ��(lJ��)'����W`c��]��&Fj�6A�f�����:�?/@��uY���,��h����u��#�w�T0Xd�ig��2vW=kU��ZOZ���\.�s���Cg�ofrUM�O�9B^%E�6��]��sV�%�җ+$���ȁ8M2v=��%���}ӁZ̞�,�l�}����0�ꡘ�WI���ˌ�����G�ǋ�<dhn�	QG��=�q��g�];7f�4+[�F�O,{����A�_���a;��4`F̅hO7&��q����I=�v�?c[����x��%�,����?��:(����B���l�+��F��W��n��%G�|K��l8���՗��9�9�F����l?�Sԙ�0e�
X!�W��M������{����g��'bT�         f   x�%���0痏A��(���%���2����t�k���j��o��9~`���JzX�k2`f�Ty�"n�$��t-�����O7�u�6!�Kd#�     