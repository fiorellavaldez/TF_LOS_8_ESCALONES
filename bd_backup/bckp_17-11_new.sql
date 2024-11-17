PGDMP      #            
    |            8_escalones    17.0    17.0 *    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16624    8_escalones    DATABASE     �   CREATE DATABASE "8_escalones" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "8_escalones";
                     postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                     postgres    false            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                        postgres    false    5            �            1259    16625    escalon_partida    TABLE     |   CREATE TABLE public.escalon_partida (
    nro_escalon integer NOT NULL,
    estado boolean NOT NULL,
    id_tema integer
);
 #   DROP TABLE public.escalon_partida;
       public         heap r       postgres    false    5            �            1259    16628    jugador    TABLE     �   CREATE TABLE public.jugador (
    id_jugador integer NOT NULL,
    nombre_jugador character varying NOT NULL,
    avatar character varying NOT NULL
);
    DROP TABLE public.jugador;
       public         heap r       postgres    false    5            �            1259    16633    jugador_id_jugador_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_id_jugador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.jugador_id_jugador_seq;
       public               postgres    false    5    218            �           0    0    jugador_id_jugador_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.jugador_id_jugador_seq OWNED BY public.jugador.id_jugador;
          public               postgres    false    219            �            1259    16634    jugador_partida    TABLE     �   CREATE TABLE public.jugador_partida (
    id_partida integer NOT NULL,
    id_jugador integer NOT NULL,
    ronda1 integer DEFAULT 0 NOT NULL,
    ronda2 integer DEFAULT 0 NOT NULL
);
 #   DROP TABLE public.jugador_partida;
       public         heap r       postgres    false    5            �            1259    16637    jugador_partida_id_partida_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_partida_id_partida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.jugador_partida_id_partida_seq;
       public               postgres    false    5    220            �           0    0    jugador_partida_id_partida_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;
          public               postgres    false    221            �            1259    16638    pregunta_partida    TABLE     h   CREATE TABLE public.pregunta_partida (
    id_pregunta integer NOT NULL,
    estado boolean NOT NULL
);
 $   DROP TABLE public.pregunta_partida;
       public         heap r       postgres    false    5            �            1259    16641 	   preguntas    TABLE     �  CREATE TABLE public.preguntas (
    id_pregunta integer NOT NULL,
    enunciado_pregunta character varying(255) NOT NULL,
    rta_a character varying(50) NOT NULL,
    rta_b character varying(50) NOT NULL,
    rta_c character varying(50) NOT NULL,
    rta_d character varying(50) NOT NULL,
    rta_correcta character varying(50) NOT NULL,
    tipo_pregunta character varying(100),
    estado_pregunta boolean,
    id_tema integer NOT NULL
);
    DROP TABLE public.preguntas;
       public         heap r       postgres    false    5            �            1259    16646    preguntas_id_pregunta_seq    SEQUENCE     �   CREATE SEQUENCE public.preguntas_id_pregunta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.preguntas_id_pregunta_seq;
       public               postgres    false    5    223            �           0    0    preguntas_id_pregunta_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;
          public               postgres    false    224            �            1259    16647    temas    TABLE     �   CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL,
    estado_tema boolean
);
    DROP TABLE public.temas;
       public         heap r       postgres    false    5            �            1259    16650    temas_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.temas_id_tema_seq;
       public               postgres    false    225    5            �           0    0    temas_id_tema_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;
          public               postgres    false    226            8           2604    16651    jugador id_jugador    DEFAULT     x   ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);
 A   ALTER TABLE public.jugador ALTER COLUMN id_jugador DROP DEFAULT;
       public               postgres    false    219    218            9           2604    16652    jugador_partida id_partida    DEFAULT     �   ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);
 I   ALTER TABLE public.jugador_partida ALTER COLUMN id_partida DROP DEFAULT;
       public               postgres    false    221    220            <           2604    16653    preguntas id_pregunta    DEFAULT     ~   ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);
 D   ALTER TABLE public.preguntas ALTER COLUMN id_pregunta DROP DEFAULT;
       public               postgres    false    224    223            =           2604    16654    temas id_tema    DEFAULT     n   ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);
 <   ALTER TABLE public.temas ALTER COLUMN id_tema DROP DEFAULT;
       public               postgres    false    226    225            �          0    16625    escalon_partida 
   TABLE DATA           G   COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
    public               postgres    false    217   �0       �          0    16628    jugador 
   TABLE DATA           E   COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
    public               postgres    false    218   �0       �          0    16634    jugador_partida 
   TABLE DATA           Q   COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
    public               postgres    false    220    2       �          0    16638    pregunta_partida 
   TABLE DATA           ?   COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
    public               postgres    false    222   =2       �          0    16641 	   preguntas 
   TABLE DATA           �   COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
    public               postgres    false    223   Z2       �          0    16647    temas 
   TABLE DATA           B   COPY public.temas (id_tema, nombre_tema, estado_tema) FROM stdin;
    public               postgres    false    225   7       �           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);
          public               postgres    false    219            �           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public               postgres    false    221            �           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 1, false);
          public               postgres    false    224            �           0    0    temas_id_tema_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.temas_id_tema_seq', 33, true);
          public               postgres    false    226            ?           2606    16729 $   escalon_partida escalon_partida_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.escalon_partida
    ADD CONSTRAINT escalon_partida_pkey PRIMARY KEY (nro_escalon);
 N   ALTER TABLE ONLY public.escalon_partida DROP CONSTRAINT escalon_partida_pkey;
       public                 postgres    false    217            C           2606    16656 $   jugador_partida jugador_partida_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT jugador_partida_pkey PRIMARY KEY (id_partida);
 N   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT jugador_partida_pkey;
       public                 postgres    false    220            A           2606    16658    jugador jugador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id_jugador);
 >   ALTER TABLE ONLY public.jugador DROP CONSTRAINT jugador_pkey;
       public                 postgres    false    218            E           2606    16733 &   pregunta_partida pregunta_partida_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.pregunta_partida
    ADD CONSTRAINT pregunta_partida_pkey PRIMARY KEY (id_pregunta);
 P   ALTER TABLE ONLY public.pregunta_partida DROP CONSTRAINT pregunta_partida_pkey;
       public                 postgres    false    222            G           2606    16660    preguntas preguntas_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);
 B   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT preguntas_pkey;
       public                 postgres    false    223            I           2606    16662    temas temas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);
 :   ALTER TABLE ONLY public.temas DROP CONSTRAINT temas_pkey;
       public                 postgres    false    225            J           2606    16734    jugador_partida fk_id_jugador    FK CONSTRAINT     �   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT fk_id_jugador FOREIGN KEY (id_jugador) REFERENCES public.jugador(id_jugador) NOT VALID;
 G   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT fk_id_jugador;
       public               postgres    false    4673    220    218            K           2606    16663    preguntas id_tema    FK CONSTRAINT        ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT id_tema FOREIGN KEY (id_tema) REFERENCES public.temas(id_tema) NOT VALID;
 ;   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT id_tema;
       public               postgres    false    225    4681    223            �   &   x�3�L���2�P��B�B(3e�, T� r��      �   7  x�U�Kr�0���)zȃGY�0,�0â�nTl��cg�6]�"=k����?��~I��X	7*�)O�g�]��a�5jdD`G"xQ�JFPud降K�
�zK��*�%R�>�
��҆�L�Hwl{<UZpz�e����,��`�h-�F3vm�:�p���|� o��Gp�9no��vV�b�� �xW'�(d�Eۄl�����@�������M'|ş�����!e��Ғ�o`۔,K���C8�2�%���+H��S�U[����0�)^�ѣh�����4���|�I��)1�Rc�y���ݘ      �      x������ � �      �      x������ � �      �   �  x��V�R9=���lm1`>��a!��K{F�h��4�.��8���U;?��e1�^dI�Q�~���3��?�n�Z9�J*#k�+��.�m�,�4.���P��?���PN<ͨ�����Xq��/��Ha�m�8+����Â� ��\EA���T��g#q!>]�lk���ۯ��oN�t�>1�7U��v��Z�0����P��m����lG��n�����(w�K�	�_%C���	Y�=��O2r�L�dũ�}�X�����l�C�䕾'��@��l����=�8"3q����qlL�`9�@L-n��H��j�L�5��E�s���)�m|cKC���ncht�I�шc#)V`%Q��:�� ��r=�N/>����:�8�*Pn���N��Ab��4�rRqQVLre �X���3��S���n��S1v�m�-�{�w���5WI�$O"'./�-��Pd��mY��vk��k�*�^O��#��-T�0X��'�ޔ����p���Ti�gF��b���g�;B?��[S�d�N�X��QI�M���}�wJ�1hZj�zCw�7ب�i�Brz#ub:4�x�TfU��(��8#F.(q���w?�O�F?���.�vF1������F��w��MC?��|�`ϲU �l}� �5�\�*�h��
RY����C�_�E���&=�n���uv6�>�+��*���6\+(9վz]p�Hy��0)P�SWqm��b�cA A���Ld�< К�Mk{�����1�V:�1-+ia�A�3y��d�L��i��ԩ�*��8,��b��������
X'��$�'���9��T#d��A�,�3�C��T+��T��P��Jub�W�/]X_�l����?�|5���q-Ԑ��V]��X�5�M���e�Z5�������[gT���!PX+�x)�a��d�������븓��U�H�a�x��Z�'���Jp����G�WL:o��[S���pB�}G����,�V���*ᱯn�m���>�N����Ë�D*�P���nfZ�F��8��brJV~��7�����#�M3+t����5�؍��s,��iԯR�ԟ��<�1�Бsq�oah�'�vnء Weu��;����`������]b^�ۇ
�ý.�K]7h�s��Oei������Z���AӃg�?�������gK      �   0  x�UQ9n�0�W����Y:����\���P�CQ�O�*]Z~,���8��3�K�T;cI���q8�)���m�s�jI����k�PX��
��ߎ��*sx"��#E����֡�2�h��<��Xׁ5���F�r�cS�=�`ۨ�69�ª�r�I�M5��l�o�`�f�'ej3.��pO��^�V#	{ߎ1�
6����
��$ݟg
G]�&�����9�������p�S�6:�\��ތLs���,|	����7_AA.�X���H!G�<�	�"�O��~��T�Rќ��|����.˲?M��V     