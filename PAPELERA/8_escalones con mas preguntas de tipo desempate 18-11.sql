PGDMP  ;    +            
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
    public               postgres    false    223   �N       '           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);
          public               postgres    false    219            (           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public               postgres    false    221            )           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 168, true);
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
��҆�L�Hwl{<UZpz�e����,��`�h-�F3vm�:�p���|� o��Gp�9no��vV�b�� �xW'�(d�Eۄl�����@�������M'|ş�����!e��Ғ�o`۔,K���C8�2�%���+H��S�U[����0�)^�ѣh�����4���|�I��)1�Rc�y���ݘ            x������ � �            x������ � �            x��\�r�ȵ}��q�R��gDI�����Ͷ4��(ۓT^�@�l	@c��R�%p>~�C�o�r��ՍA�I�
ɾ���k�ޘA��{�����O�X�S��Ne���&"�Y��"|UJcDx�7J$��`okȗ=�l�2����61�O�Z~��i)C���Q�4�#��eV�0�a�mxb��L��~p01b.��\e�N����f&�w��U6+t��u*lx&�Si,n��y�"����v$�,�4�sJ�,?g��.��;�7�7��a��}��F��(�r�.?����([,�LD�d�%^K�-?fxk��'��{��n�1I"2i�j��6/#���j�a� �p#:�71I�҈,�����=º���`#�ˏI���l1�U�8ǽv�YW�A"S�)��0J�x]f3��,7;>�)-^��F�� )�&��I�	 �H���~p���R:�r+dY\�_J%2��x�%2���Z�}qXN�I��tfUTb��EF��ZP���ƠY�ޚ��(bj�n:B��$�˅��d����B$
6ita��s��ݏ���n�����{�:�:,D���6a-m|%8��-𥉉p�M-.?%3�dp�M)g�^����%N���qy���u��^ۘ�����������q�	��,����_� �t���{l��@�9,2�X<=��΅��Q�j�;TV���R�=K@G�nU�#����v��5MTTx_�;)?���7�I�Wo��B%�jN$"8jF�g>on���!<9��͛=��V�"i��5,�J��7#�`{��ls౹k��P��*����i�KI�<ᔋ݇��E�bP�\g�=n��w)����"�������Gs|;<�V�ju�6��-K�/A���u"��C�	8F!����X:�L��M��]�ݻ�R�jֽ�N�{Z�f�5�B�2/�5-Q�;��l�e���u܂��t�E��5I���.���=���F�P���]C�p.D%  ��Ѧ�_ �~ Wú`�m>�<����kt�Ӈi\�D��
F��T6L5T�9w�ݣ����6������0I'��(gif�)�&���GΠW˵C�sDm��%��e���+��:����Z�sxsHbhNa���ĊL���X2"��V�#@�F��w9�N�?���'LH�,��	n��6x��i;�vg
�,�Ȕ7.�}W��rsc�ۉ��(�T��'؅i�6!�"�	c�7CQ$�P�D
�b�kqMy����F���6��A�r�^7��t-//ݟ�H$�a"O\(���#�w3�
��ak����]� �.+`˚���N6"��v��6��ӎ�[#x��܈�@"`:�"ƀ0�&x)a���{ez��r.!{��{O��:s���[��
��b^��h}$2/?V0��lkŵ�,�^M�S$
.5�ʄ���0d�"��N���������cP�4z*�	���o@Ʒ�bk�k�2i���9�y��a��(�eh����9����=6lw))����@����2f<���-���i;�s��68�5!�0�D�3��8gp�y��s��Jk�;�/���L���NjU.Ӭz�?���r6y �����,a`3-M?���$vP\��[�v�a����!P�0�dD�(eR�y���H������4O@��S���]�(�Kp@��I?.�\\�P򞫬�ҹ@(@�H>�)$@�w� $��@��P�bB|M�[%�d���ST
�z���Yq�J��rT��	o�`�.���ra�Sn�\a/�Q1&����\�5�4IV���%�L
��ಟ5ދǒaqe�c�,�=�op���5f�؅yE���'uf��6{GRf���F�Yq-.zz��.�G�AW����ʝqi>����Z
� y��fZ�p�j���f[���|���j/N۫�v���OE��������}�� T`������l�$���JY��D~���(�L��1�gD�!e��@]��[	�G� Zw���r�&�k�Y���5Q��sL��Fc��1�u9!�,����ޙ��- �d��{d$x������5ocn��5� `$ȍ�=lE�����.`o�l��	�ИQ�D�X��� 9X����5v�H��#@�t�۽��l%-	�g*?�?�f�c�B��@�3\�:e���� Q�$<r��@�b�bܟ"L"B�RDA�Xo�B:�n}�L[����m�����z��H&JڶO͜Y���� ���'��d����v_�rV*V�2���a:��V���p�fձӄ��BP޶�T�++a��6)J��A�� O��ٻ�H��X&�q#z<$���"Fe|��}�5ǌ��~�_�eDl}�?�ɾ��~6�Z�#�.Dyd���L�3|�B̠��u�m�2�N �2��-�;m[o�BAT1���-?�ˢ��a�e�
�s��j�Z��0��\�V��hf�Ǜ�/\Ѓ��ϙ�Lh�]�>Ӏ����S���E�y�D+�^x�t:1���MaI��ޞ�9�i�>�L�U����8�O���&A�G���T]vFPM`$��w����i�ݦ�xh���f�B듼���L�����r�5�Y�H������@�=���n<��Ɨ��>� `�Ed������*S�~6��4�r0'�>��a~�~�1�<�sԺ�,�1u�"���s���g;A?oi�l�����q&��Lti`vȏ&��"ٟީ��D�җ�
ɮ0�<�h��J�{)Y3�f��k��3|��3�p�GΪ=)�j��_��Ċ ��[�3���Tv�꧅#�5.Ԁq\��uzF���4��^��ʊ{��,�[m�;Q5�`��J�'�!nR'���q<�ȃ$�dj�7��4��;��s�P�z��$z5s�	�U+�T��F���R�O��*��qx���WFF뢼�Cʛ�B�#�W,)^x!c�
6!��s���ő0j�AW�@<�C��|����
���#~
C�?�"%-�Vd��4�%l׻�_U:�R6{}õ*�߇I �`���!*�*
�^oac�O�i�=�K��R�O%��!��oK���Of*gr`�cw�����r�T��H
�"z'�,0���n��p����"�Qe	㠞�_C�BU�[�s%��gpm��1�AR�X��V��n:�~���&,�.�i�Z����ZG#�����+� 3$ �X�[�`�����w����Ч</�{�#^3#P�c?L�q�Vh�;i!a�λI!��2+�>,��/�'�HV����nO����;T�٤�H�y8XQi �A������`���@z�c�k8>xQ%��P��*h��R�ft@��'#%��Xu��<�� �*']���V;|���S��R<��%z�˥9�tK�T؎[t��1� �w���3�m3ɓ\���ѿ��^�ı��!W�$�t�y��������/E�LtG�����̘��Q~o �y�SGڈGV����l<2	^c$�͞�zz.��	���DBQ-�Q���[y�2��%�;A���f��t��jc}"�o��c�6��9�E2�8E����8Q���Jx*ʼWY��&2�V����{8,�?���e��y�D�f�`N"�I{��)/qQ�v��P�T�&��M���YLdܙl��4gw��3�i����v��G�q�QU�o����f�`�\�"����;����gpEmd%�$2*�!�,�ŵ�����_rwM�EW�x�Q*q�ă�h���&*a��4���+��4��|ӕk����X�j�&㝗����0?"��s*źp0��x���w�i���fE}
KxWD�.��)�y�����<�iL�u��9�{ܑW�J.3���koi<��
'�'5�o��Cw��)[e�2��)3Y،Ai�E["���Y&�0!��LɁ�"P1^֦���%����tY��
x޼���/.�������ح�6�� �]�����24�Fފ-��9�3c�S7�d4�v��H�@C�n�an�
d�   ��<�k|YD�D {1����E�BF8�Y�z�f�V�*�$k�\�����yp�t�]���)Yx�|�(@��Ȕ�9�����N@0�T�d:b����V���*��fm�wHN�K�'����|�V'�_a�2���g���n*��%�d���||��l^<Ha�;��3�f��X�C8�|���Fn�\k���fJ�jsx��U���v��/	�Ky���/:{Ξɲ�8G0D�:slH�r,+YX��Z�si�K1?��3�E��E�\H:�T�F��X�A8����*����# I+�%|�M+_v�ꔽ��νYA�v�u
�/�P±Jsȝ=/H2����=u��w�8��#�>%�l��Pg��d�l�WT��Y�~�ɇ��|�-�������3��5�uf�v�)����o� �S:< ���e�	U�<��G\K,5�J���Z����j&�J��f���[�x\J�"H�!�ᕁ���2��^C�!X/	��P���V��1A�8dx�w��2�2_�����r��l"�t�"c��f�POx&zy\��}X�lxXIHO^k݀�`�%����\���|�9��R�'B%n�-�paX�d��2���W%�@G��`˄��X����C$Eu̇Cwd��'�A��9��6�ˁ�ռ4�Qf�t�O�����r^�1s���3�np�ÿ��C�K��P���;���.�Z>"Y՜;>~��D_�̵���CLPS�$?N2��)$�"�@��Y;�`�!g�լ*1�M[i!����ᡈ��w��� ���� e�\���j�N�������9B	�����`}�mU@�_�e��|s�<<�)�D���X� ��6x!
�>���:��\�[;V���sK�z 9u�k�vnw(����2�h��~r.���ә��<^d�G#�X}eL�D�Ol+��h������ 5����sC��U�u�{���#8g��C��q��R�~�� �T݁y�l�"���<�<����I�a���4YL�I�I�U#��p��D������~�m���)�	�����J~#L� �s�4o�HІ�. ��3�s{K����	236�';�o��BB������O\,�{��G��P�u)N�L�s85-+����gY~ŷ䰧$=̝�乀~�� Ǳ�s�����\}D�ys,�e�McAib��5�I�ӂC�I�+���L�(�D�0�9p�j�)�����[�2�
КT=�8���.@�B�{:�Ip5�9zq�Odc~�����,�r���@|��lVNr֪~����]F��a���YXu��,�S�9+k���n�w�1��y�y[l�̪��<Ev��UR�u�s��p�|*�\��$���u��0ķZ�l��pM�Lw�m7��6����?��!��߼x�x�ߝ��Y�B$�T�X�*B��K��
���}N�!'.(�3X/�@l/af�Z����LD2�)p�ڦO*��f� �m &YG��q)��9�nS�+f.�<,'� w}!�ԇ�l��d��تC�w1�##yy��ʑ����q^rk��d����X~D����C.��k8�ӟ� ���@�neO��3-�§�c����"��\��zIK۬ɮY�~���~������iw��O�O�W�@]�%�ȩ��$[(D ^�/�� F��L�ٌ$�$E��٬~���T i;��<<�ڮm�+��R�� M[G<b���;лb���If�g`�S[;<���?���N���ԧ�z+���d�{�yc[X2���3�e۟���*tl|��x5y�dYң	��������yp6��~�E�^�csͽR	~�z�(��,�E"@r�H�`�Ĳ)E
,����|Uie0H�ˤ��[�������H�$��3��}�"����(ZjŎk5�q���MAE�K�R�̵)<��I��B9e�m]*��]S���:xY�p���p�<cR�nn��2��jyQ�s��g���Mѹ����R�V��D<�9�fI���%�kٹ �@��9D["vU���)��Y=y��%g)���y.dXF��aq邏��|#�a1F�m�#È�D�x�uLn&s�aƕ�۱�����L̙��X�y�s��R��g8���	M���RV�@�7�1L���L�Ņ�������t�I�O�:GI�z�uL�a4���uH��N�
1�_MT��]�Gљ�`u,+[����F|�*�xu��3Ĉ��6�51Ymo�e5�����Z��Zqf��b�ʪ~,䤝�`�3�y�¸��C���n-��>�W��i*��������>�p��u�p����;W= �U��g�' �W��o�
s���c�+�w�㧴�̷�ٝ�ȕ���I��j�;l��ވ�Y
�G��՟�\�W}А������]ҷB�*�:F�ݯ5w�sՑNWz��0�S�3�*Qؔt�SNX�J�?���d+�v;LL�m�"��|���u,^�d!�<6�!3Y��z�5޳ ֹ���߁S�`�]g�m���]�0�U%�j=h��)9+�s�	��g�ob]M�'�!���s��Ӯb�9�ڒ�����
�8��NҜ]|�ⱤW�_:PKس��Ӂ��ϴ���V=��*�B���;�3z�~r��	���#�[lBT��|�}���w�΍EG-��֨������s����b�8l��̈���ZGs>��
��s���ҟ��]4(g)\����L�A��}��,?"�ldدh7q������%G�|K��l8���՗��9�~F���
��~u!��lX+����D?�ol���ў�_{���"v�����C��ǂ�r�(��j�F��y�?<:��)vw6V��k\y��?Q7W�:\}*�j���my��ѸR�}z�;#H��b0\yV�Kw�m+=W3��I穷��c_t�C�-�����Vkk
�sG�676�{+6+uW@��)�n/������菔����w�֧�������f�Ď H�K��M�=,]�q�L��ͽ�s0|�iȦ������'G 78�9�X��7����3M�����Ã?�N����N��нBJ��i+�`Q3Xq\)�0�����<d���e��"+0��{�a�K4�Yy��{^ճ�ڄ�0M��U�t7���k�
c�-O5�z~���r�'�k��7ʟ=�0�k�HJ�	��a�`�]�[ ��¹�K��D(	O=\�����U5��Q�c��8a�/¶����^�$��k���꺬3b$�����
հkU=�N��Hw0�S�f?�F�4K�එ�;��Xur!���՝�j��\�ΐ߇�����e��]�H�5��k���-}}��zD��+�����"y�Qx�&��\V��W��2�c��$�:B�_��{������N��P,��#ҷ�W��,��A�t�	w\�j�ֿk��+�.-ޮ?\�6��@�#:䝹�7�[�� *ER%'���h��+~	�U�֦�흅�a���p+]�͈߹�_�g���\պ�UwNyq��Tk/�����u����Ϟ=�ҽV         f   x�%���0痏AjK)+�~ �U��C��������n�Kj�!҈���'��pFf۝>=�q֭�O�`��dXsV�Յ61m�L5��J�ާ��f0$@     