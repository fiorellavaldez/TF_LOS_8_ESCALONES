toc.dat                                                                                             0000600 0004000 0002000 00000030053 14716411753 0014451 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP   7                
    |            8_escalones    17.0    17.0 *    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false         �           1262    16624    8_escalones    DATABASE     �   CREATE DATABASE "8_escalones" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "8_escalones";
                     postgres    false                     2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                     postgres    false         �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                        postgres    false    5         �            1259    16625    escalon_partida    TABLE     |   CREATE TABLE public.escalon_partida (
    nro_escalon integer NOT NULL,
    estado boolean NOT NULL,
    id_tema integer
);
 #   DROP TABLE public.escalon_partida;
       public         heap r       postgres    false    5         �            1259    16628    jugador    TABLE     �   CREATE TABLE public.jugador (
    id_jugador integer NOT NULL,
    nombre_jugador character varying NOT NULL,
    avatar character varying NOT NULL
);
    DROP TABLE public.jugador;
       public         heap r       postgres    false    5         �            1259    16633    jugador_id_jugador_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_id_jugador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.jugador_id_jugador_seq;
       public               postgres    false    5    218         �           0    0    jugador_id_jugador_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.jugador_id_jugador_seq OWNED BY public.jugador.id_jugador;
          public               postgres    false    219         �            1259    16634    jugador_partida    TABLE     �   CREATE TABLE public.jugador_partida (
    id_partida integer NOT NULL,
    id_jugador integer NOT NULL,
    ronda1 integer DEFAULT 0 NOT NULL,
    ronda2 integer DEFAULT 0 NOT NULL
);
 #   DROP TABLE public.jugador_partida;
       public         heap r       postgres    false    5         �            1259    16637    jugador_partida_id_partida_seq    SEQUENCE     �   CREATE SEQUENCE public.jugador_partida_id_partida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.jugador_partida_id_partida_seq;
       public               postgres    false    5    220         �           0    0    jugador_partida_id_partida_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;
          public               postgres    false    221         �            1259    16638    pregunta_partida    TABLE     h   CREATE TABLE public.pregunta_partida (
    id_pregunta integer NOT NULL,
    estado boolean NOT NULL
);
 $   DROP TABLE public.pregunta_partida;
       public         heap r       postgres    false    5         �            1259    16641 	   preguntas    TABLE     �  CREATE TABLE public.preguntas (
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
       public         heap r       postgres    false    5         �            1259    16646    preguntas_id_pregunta_seq    SEQUENCE     �   CREATE SEQUENCE public.preguntas_id_pregunta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.preguntas_id_pregunta_seq;
       public               postgres    false    5    223         �           0    0    preguntas_id_pregunta_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;
          public               postgres    false    224         �            1259    16647    temas    TABLE     �   CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL,
    estado_tema boolean
);
    DROP TABLE public.temas;
       public         heap r       postgres    false    5         �            1259    16650    temas_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.temas_id_tema_seq;
       public               postgres    false    225    5         �           0    0    temas_id_tema_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;
          public               postgres    false    226         8           2604    16651    jugador id_jugador    DEFAULT     x   ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);
 A   ALTER TABLE public.jugador ALTER COLUMN id_jugador DROP DEFAULT;
       public               postgres    false    219    218         9           2604    16652    jugador_partida id_partida    DEFAULT     �   ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);
 I   ALTER TABLE public.jugador_partida ALTER COLUMN id_partida DROP DEFAULT;
       public               postgres    false    221    220         <           2604    16653    preguntas id_pregunta    DEFAULT     ~   ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);
 D   ALTER TABLE public.preguntas ALTER COLUMN id_pregunta DROP DEFAULT;
       public               postgres    false    224    223         =           2604    16654    temas id_tema    DEFAULT     n   ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);
 <   ALTER TABLE public.temas ALTER COLUMN id_tema DROP DEFAULT;
       public               postgres    false    226    225         �          0    16625    escalon_partida 
   TABLE DATA           G   COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
    public               postgres    false    217       4829.dat �          0    16628    jugador 
   TABLE DATA           E   COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
    public               postgres    false    218       4830.dat �          0    16634    jugador_partida 
   TABLE DATA           Q   COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
    public               postgres    false    220       4832.dat �          0    16638    pregunta_partida 
   TABLE DATA           ?   COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
    public               postgres    false    222       4834.dat �          0    16641 	   preguntas 
   TABLE DATA           �   COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
    public               postgres    false    223       4835.dat �          0    16647    temas 
   TABLE DATA           B   COPY public.temas (id_tema, nombre_tema, estado_tema) FROM stdin;
    public               postgres    false    225       4837.dat �           0    0    jugador_id_jugador_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);
          public               postgres    false    219         �           0    0    jugador_partida_id_partida_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);
          public               postgres    false    221         �           0    0    preguntas_id_pregunta_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 1, false);
          public               postgres    false    224         �           0    0    temas_id_tema_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.temas_id_tema_seq', 33, true);
          public               postgres    false    226         ?           2606    16729 $   escalon_partida escalon_partida_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.escalon_partida
    ADD CONSTRAINT escalon_partida_pkey PRIMARY KEY (nro_escalon);
 N   ALTER TABLE ONLY public.escalon_partida DROP CONSTRAINT escalon_partida_pkey;
       public                 postgres    false    217         C           2606    16656 $   jugador_partida jugador_partida_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT jugador_partida_pkey PRIMARY KEY (id_partida);
 N   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT jugador_partida_pkey;
       public                 postgres    false    220         A           2606    16658    jugador jugador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id_jugador);
 >   ALTER TABLE ONLY public.jugador DROP CONSTRAINT jugador_pkey;
       public                 postgres    false    218         E           2606    16733 &   pregunta_partida pregunta_partida_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.pregunta_partida
    ADD CONSTRAINT pregunta_partida_pkey PRIMARY KEY (id_pregunta);
 P   ALTER TABLE ONLY public.pregunta_partida DROP CONSTRAINT pregunta_partida_pkey;
       public                 postgres    false    222         G           2606    16660    preguntas preguntas_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);
 B   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT preguntas_pkey;
       public                 postgres    false    223         I           2606    16662    temas temas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);
 :   ALTER TABLE ONLY public.temas DROP CONSTRAINT temas_pkey;
       public                 postgres    false    225         J           2606    16734    jugador_partida fk_id_jugador    FK CONSTRAINT     �   ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT fk_id_jugador FOREIGN KEY (id_jugador) REFERENCES public.jugador(id_jugador) NOT VALID;
 G   ALTER TABLE ONLY public.jugador_partida DROP CONSTRAINT fk_id_jugador;
       public               postgres    false    4673    220    218         K           2606    16663    preguntas id_tema    FK CONSTRAINT        ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT id_tema FOREIGN KEY (id_tema) REFERENCES public.temas(id_tema) NOT VALID;
 ;   ALTER TABLE ONLY public.preguntas DROP CONSTRAINT id_tema;
       public               postgres    false    225    4681    223                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             4829.dat                                                                                            0000600 0004000 0002000 00000000075 14716411753 0014273 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	f	\N
2	f	\N
3	f	\N
4	f	\N
5	f	\N
6	f	\N
7	f	\N
8	f	\N
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                   4830.dat                                                                                            0000600 0004000 0002000 00000001221 14716411753 0014255 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Fiore	vista/img/fi.jpg
2	Dayana	vista/img/da.jpg
3	Alexis	vista/img/al.jpg
4	Tania	vista/img/ta.png
5	Carlos	vista/img/edna.jpg
6	Bruno	vista/img/kevin.jpg
7	Facundo	vista/img/fa.jpg
8	Kadir	vista/img/ka.jpg
9	Jarrison	vista/img/jarr.jpg
10	h3ll0w0r1d	vista/img/amore.jpg
11	Pepita	vista/img/avatar.png
13	Colapinto	vista/img/caradepapa.jpeg
14	LaÄMikitá	vista/img/dory.jpeg
15	Diana	vista/img/jazmin.jpeg
18	Kika	vista/img/merida.jpeg
19	Barassi	vista/img/moana.jpeg
12	Pablo	vista/img/aladdin.jpeg
16	Luis	vista/img/goku.jpeg
17	Ale	vista/img/gohan.jpeg
21	Mili	vista/img/tiana.jpeg
22	Daria	vista/img/daria.jpg
20	Cindy Lou	vista/img/mulan.jpeg
\.


                                                                                                                                                                                                                                                                                                                                                                               4832.dat                                                                                            0000600 0004000 0002000 00000000005 14716411753 0014256 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4834.dat                                                                                            0000600 0004000 0002000 00000000005 14716411753 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4835.dat                                                                                            0000600 0004000 0002000 00000004652 14716411753 0014275 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	¿Quién fue el primer presidente de los Estados Unidos?	Abraham Lincoln	George Washington	John Adams	Thomas Jefferson	B	M	\N	1
2	¿En qué año cayó el Imperio Romano de Occidente?	410	476	512	630	B	M	\N	1
3	¿Quién fue el conquistador de los aztecas?	Cristóbal Colón	Hernán Cortés	Francisco Pizarro	Vasco Núñez de Balboa	B	M	\N	1
4	¿Cuál fue la causa principal de la Revolución Francesa?	La invasión de Inglaterra	La injusticia social	El aumento de impuestos por el papa	La conquista de territorios americanos	B	M	\N	1
5	¿Quién fue el último emperador de Roma?	Augusto	Nerón	Rómulo Augústulo	Constantino	C	M	\N	1
6	¿En qué año comenzó la Primera Guerra Mundial?	1900	1914	1920	1939	B	M	\N	1
7	¿Quién escribió la Declaración de Independencia de los Estados Unidos?	George Washington	Thomas Jefferson	Alexander Hamilton	Benjamin Franklin	B	M	\N	1
8	¿En qué país tuvo lugar la Revolución de Octubre de 1917?	China	Rusia	Francia	Alemania	B	M	\N	1
9	¿Quién fue el líder de la independencia de la India?	Gandhi	Nehru	Patel	Bose	A	M	\N	1
10	¿Qué país fue liderado por Napoleón Bonaparte?	Inglaterra	Francia	Italia	España	B	M	\N	1
11	¿Qué imperio fue derrotado por los musulmanes en 1453?	El Imperio Romano de Occidente	El Imperio Otomano	El Imperio Bizantino	El Imperio de Alejandro Magno	C	M	\N	1
12	¿En qué año se firmó la Declaración de los Derechos del Hombre y del Ciudadano?	1789	1791	1801	1812	A	M	\N	1
13	¿Quién fue el líder del Tercer Reich en Alemania?	Joseph Goebbels	Heinrich Himmler	Adolf Hitler	Erwin Rommel	C	M	\N	1
14	¿En qué ciudad se firmó el Tratado de Versalles en 1919?	Berlín	Londres	París	Roma	C	M	\N	1
15	¿Qué guerra se libró entre 1950 y 1953 en la península de Corea?	La Guerra Civil China	La Guerra de Vietnam	La Guerra de Corea	La Guerra de Japón	C	M	\N	1
16	¿Qué imperio fue conocido por sus avances en matemáticas y astronomía, y por su capital en Bagdad?	El Imperio Romano	El Imperio Otomano	El Imperio Persa	El Califato Abasí	D	M	\N	1
17	¿En qué año terminó la Segunda Guerra Mundial?	1940	1945	1950	1955	B	M	\N	1
18	¿Quién fue el primer emperador de China?	Qin Shi Huang	Liu Bang	Han Wudi	Sun Tzu	A	M	\N	1
19	¿Quién fue el dictador de la Unión Soviética durante la Segunda Guerra Mundial?	Nikita Jrushchov	Mijaíl Gorbachov	Stalin	Lenin	C	M	\N	1
20	¿Qué civilización construyó las pirámides de Egipto?	Los romanos	Los egipcios	Los griegos	Los fenicios	B	M	\N	1
\.


                                                                                      4837.dat                                                                                            0000600 0004000 0002000 00000001040 14716411753 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Historia	\N
2	Geografía	\N
3	Ciencias Naturales	\N
4	Matemáticas	\N
5	Literatura	\N
6	Música	\N
7	Cine	\N
8	Deporte	\N
9	Tecnología	\N
10	Arte	\N
11	Cultura General	\N
12	Economía	\N
13	Política	\N
14	Filosofía	\N
15	Biología	\N
16	Química	\N
17	Física	\N
18	Astronomía	\N
19	Medicina	\N
20	Ingeniería	\N
21	Ecología	\N
22	Religión	\N
23	Psicología	\N
24	Antropología	\N
25	Sociología	\N
26	Gastronomía	\N
27	Idiomas	\N
28	Mitología	\N
29	Educación	\N
30	Arquitectura	\N
33	Astrología	\N
31	Idiomas	\N
32	Novelas	\N
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                restore.sql                                                                                         0000600 0004000 0002000 00000024173 14716411753 0015404 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "8_escalones";
--
-- Name: 8_escalones; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "8_escalones" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';


ALTER DATABASE "8_escalones" OWNER TO postgres;

\connect "8_escalones"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: escalon_partida; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.escalon_partida (
    nro_escalon integer NOT NULL,
    estado boolean NOT NULL,
    id_tema integer
);


ALTER TABLE public.escalon_partida OWNER TO postgres;

--
-- Name: jugador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jugador (
    id_jugador integer NOT NULL,
    nombre_jugador character varying NOT NULL,
    avatar character varying NOT NULL
);


ALTER TABLE public.jugador OWNER TO postgres;

--
-- Name: jugador_id_jugador_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jugador_id_jugador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jugador_id_jugador_seq OWNER TO postgres;

--
-- Name: jugador_id_jugador_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jugador_id_jugador_seq OWNED BY public.jugador.id_jugador;


--
-- Name: jugador_partida; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jugador_partida (
    id_partida integer NOT NULL,
    id_jugador integer NOT NULL,
    ronda1 integer DEFAULT 0 NOT NULL,
    ronda2 integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.jugador_partida OWNER TO postgres;

--
-- Name: jugador_partida_id_partida_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jugador_partida_id_partida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNER TO postgres;

--
-- Name: jugador_partida_id_partida_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jugador_partida_id_partida_seq OWNED BY public.jugador_partida.id_partida;


--
-- Name: pregunta_partida; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pregunta_partida (
    id_pregunta integer NOT NULL,
    estado boolean NOT NULL
);


ALTER TABLE public.pregunta_partida OWNER TO postgres;

--
-- Name: preguntas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preguntas (
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


ALTER TABLE public.preguntas OWNER TO postgres;

--
-- Name: preguntas_id_pregunta_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.preguntas_id_pregunta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNER TO postgres;

--
-- Name: preguntas_id_pregunta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.preguntas_id_pregunta_seq OWNED BY public.preguntas.id_pregunta;


--
-- Name: temas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temas (
    id_tema integer NOT NULL,
    nombre_tema character varying(100) NOT NULL,
    estado_tema boolean
);


ALTER TABLE public.temas OWNER TO postgres;

--
-- Name: temas_id_tema_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.temas_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.temas_id_tema_seq OWNER TO postgres;

--
-- Name: temas_id_tema_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.temas_id_tema_seq OWNED BY public.temas.id_tema;


--
-- Name: jugador id_jugador; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador ALTER COLUMN id_jugador SET DEFAULT nextval('public.jugador_id_jugador_seq'::regclass);


--
-- Name: jugador_partida id_partida; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador_partida ALTER COLUMN id_partida SET DEFAULT nextval('public.jugador_partida_id_partida_seq'::regclass);


--
-- Name: preguntas id_pregunta; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preguntas ALTER COLUMN id_pregunta SET DEFAULT nextval('public.preguntas_id_pregunta_seq'::regclass);


--
-- Name: temas id_tema; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temas ALTER COLUMN id_tema SET DEFAULT nextval('public.temas_id_tema_seq'::regclass);


--
-- Data for Name: escalon_partida; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM stdin;
\.
COPY public.escalon_partida (nro_escalon, estado, id_tema) FROM '$$PATH$$/4829.dat';

--
-- Data for Name: jugador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM stdin;
\.
COPY public.jugador (id_jugador, nombre_jugador, avatar) FROM '$$PATH$$/4830.dat';

--
-- Data for Name: jugador_partida; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM stdin;
\.
COPY public.jugador_partida (id_partida, id_jugador, ronda1, ronda2) FROM '$$PATH$$/4832.dat';

--
-- Data for Name: pregunta_partida; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pregunta_partida (id_pregunta, estado) FROM stdin;
\.
COPY public.pregunta_partida (id_pregunta, estado) FROM '$$PATH$$/4834.dat';

--
-- Data for Name: preguntas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM stdin;
\.
COPY public.preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema) FROM '$$PATH$$/4835.dat';

--
-- Data for Name: temas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temas (id_tema, nombre_tema, estado_tema) FROM stdin;
\.
COPY public.temas (id_tema, nombre_tema, estado_tema) FROM '$$PATH$$/4837.dat';

--
-- Name: jugador_id_jugador_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jugador_id_jugador_seq', 22, true);


--
-- Name: jugador_partida_id_partida_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jugador_partida_id_partida_seq', 1, false);


--
-- Name: preguntas_id_pregunta_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.preguntas_id_pregunta_seq', 1, false);


--
-- Name: temas_id_tema_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temas_id_tema_seq', 33, true);


--
-- Name: escalon_partida escalon_partida_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.escalon_partida
    ADD CONSTRAINT escalon_partida_pkey PRIMARY KEY (nro_escalon);


--
-- Name: jugador_partida jugador_partida_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT jugador_partida_pkey PRIMARY KEY (id_partida);


--
-- Name: jugador jugador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id_jugador);


--
-- Name: pregunta_partida pregunta_partida_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pregunta_partida
    ADD CONSTRAINT pregunta_partida_pkey PRIMARY KEY (id_pregunta);


--
-- Name: preguntas preguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT preguntas_pkey PRIMARY KEY (id_pregunta);


--
-- Name: temas temas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temas
    ADD CONSTRAINT temas_pkey PRIMARY KEY (id_tema);


--
-- Name: jugador_partida fk_id_jugador; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador_partida
    ADD CONSTRAINT fk_id_jugador FOREIGN KEY (id_jugador) REFERENCES public.jugador(id_jugador) NOT VALID;


--
-- Name: preguntas id_tema; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preguntas
    ADD CONSTRAINT id_tema FOREIGN KEY (id_tema) REFERENCES public.temas(id_tema) NOT VALID;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     