PGDMP  6    #            
    |         
   NewFinalDB    17.1    17.1 ^    g           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            h           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            i           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            j           1262    16868 
   NewFinalDB    DATABASE     �   CREATE DATABASE "NewFinalDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE "NewFinalDB";
                     postgres    false                        2615    16869 
   TempSchema    SCHEMA        CREATE SCHEMA "TempSchema";
    DROP SCHEMA "TempSchema";
                     postgres    false            �            1259    16870    AsistenciaEstudiante    TABLE     �   CREATE TABLE "TempSchema"."AsistenciaEstudiante" (
    "CodigoH" integer NOT NULL,
    "IDEstudiante" integer NOT NULL,
    "Fecha" date NOT NULL,
    "Asiste" boolean DEFAULT false NOT NULL
);
 0   DROP TABLE "TempSchema"."AsistenciaEstudiante";
    
   TempSchema         heap r       postgres    false    6            �            1259    16874    AsistenciaUsuario    TABLE     �   CREATE TABLE "TempSchema"."AsistenciaUsuario" (
    "CodigoH" integer NOT NULL,
    "IDUsuario" integer NOT NULL,
    "Fecha" date NOT NULL,
    "Asiste" boolean DEFAULT false NOT NULL
);
 -   DROP TABLE "TempSchema"."AsistenciaUsuario";
    
   TempSchema         heap r       postgres    false    6            �            1259    16878    Aula    TABLE       CREATE TABLE "TempSchema"."Aula" (
    "Grupo" integer NOT NULL,
    "GradoT" character varying,
    "GradoNum" character varying,
    "GrupoEquivalente" character varying,
    "Jornada" character varying,
    "Año" integer,
    "CodigoInsti" bigint,
    "IDUsuario" integer
);
     DROP TABLE "TempSchema"."Aula";
    
   TempSchema         heap r       postgres    false    6            �            1259    16883    Aula_Grupo_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Aula_Grupo_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE "TempSchema"."Aula_Grupo_seq";
    
   TempSchema               postgres    false    6    220            k           0    0    Aula_Grupo_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE "TempSchema"."Aula_Grupo_seq" OWNED BY "TempSchema"."Aula"."Grupo";
       
   TempSchema               postgres    false    221            �            1259    16884 
   Estudiante    TABLE     �  CREATE TABLE "TempSchema"."Estudiante" (
    "IDEstudiante" bigint NOT NULL,
    "TipoID" character varying,
    "PrimerNombre" character varying(20),
    "SegundoNombre" character varying(20),
    "PrimerApellido" character varying(20),
    "SegundoApellido" character varying(20),
    "Genero" character varying(10),
    "FechaNacimiento" date,
    "Estrato" integer,
    "Año" integer,
    "Grupo" integer
);
 &   DROP TABLE "TempSchema"."Estudiante";
    
   TempSchema         heap r       postgres    false    6            �            1259    16889    EstudianteTieneHorario    TABLE     |   CREATE TABLE "TempSchema"."EstudianteTieneHorario" (
    "CodigoH" integer NOT NULL,
    "IDEstudiante" integer NOT NULL
);
 2   DROP TABLE "TempSchema"."EstudianteTieneHorario";
    
   TempSchema         heap r       postgres    false    6            �            1259    16892    Estudiante_IDEstudiante_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Estudiante_IDEstudiante_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE "TempSchema"."Estudiante_IDEstudiante_seq";
    
   TempSchema               postgres    false    6    222            l           0    0    Estudiante_IDEstudiante_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE "TempSchema"."Estudiante_IDEstudiante_seq" OWNED BY "TempSchema"."Estudiante"."IDEstudiante";
       
   TempSchema               postgres    false    224            �            1259    16893    Examen    TABLE     �   CREATE TABLE "TempSchema"."Examen" (
    "IDEvaluacion" integer NOT NULL,
    "Nota" double precision,
    "BloqueLectivo" character varying,
    "Año" integer,
    "IDEstudiante" integer,
    "IDUsuario" integer
);
 "   DROP TABLE "TempSchema"."Examen";
    
   TempSchema         heap r       postgres    false    6            �            1259    16898    Examen_IDEvaluacion_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Examen_IDEvaluacion_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE "TempSchema"."Examen_IDEvaluacion_seq";
    
   TempSchema               postgres    false    6    225            m           0    0    Examen_IDEvaluacion_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE "TempSchema"."Examen_IDEvaluacion_seq" OWNED BY "TempSchema"."Examen"."IDEvaluacion";
       
   TempSchema               postgres    false    226            �            1259    16899    Horario    TABLE     ?  CREATE TABLE "TempSchema"."Horario" (
    "CodigoH" integer NOT NULL,
    "FechaInicio" date NOT NULL,
    "FechaFin" date NOT NULL,
    "HoraInicio" time without time zone NOT NULL,
    "HoraFin" time without time zone NOT NULL,
    "DiaInicial" character(1) NOT NULL,
    "DiaTexto" character varying(10) NOT NULL
);
 #   DROP TABLE "TempSchema"."Horario";
    
   TempSchema         heap r       postgres    false    6            �            1259    16902    HorarioTieneAula    TABLE     o   CREATE TABLE "TempSchema"."HorarioTieneAula" (
    "CodigoH" integer NOT NULL,
    "Grupo" integer NOT NULL
);
 ,   DROP TABLE "TempSchema"."HorarioTieneAula";
    
   TempSchema         heap r       postgres    false    6            �            1259    16905    Horario_CodigoH_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Horario_CodigoH_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE "TempSchema"."Horario_CodigoH_seq";
    
   TempSchema               postgres    false    6    227            n           0    0    Horario_CodigoH_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE "TempSchema"."Horario_CodigoH_seq" OWNED BY "TempSchema"."Horario"."CodigoH";
       
   TempSchema               postgres    false    229            �            1259    16906    Institucion    TABLE     4  CREATE TABLE "TempSchema"."Institucion" (
    "CodigoInsti" bigint NOT NULL,
    "NombreInsti" character varying(100),
    "NombreRector" character varying(100),
    "Localidad" character varying,
    "Barrio" character varying,
    "Numero" integer,
    "Direccion" character varying,
    "Año" integer
);
 '   DROP TABLE "TempSchema"."Institucion";
    
   TempSchema         heap r       postgres    false    6            �            1259    16911    Institucion_CodigoInsti_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Institucion_CodigoInsti_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE "TempSchema"."Institucion_CodigoInsti_seq";
    
   TempSchema               postgres    false    6    230            o           0    0    Institucion_CodigoInsti_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE "TempSchema"."Institucion_CodigoInsti_seq" OWNED BY "TempSchema"."Institucion"."CodigoInsti";
       
   TempSchema               postgres    false    231            �            1259    16912    Persona    TABLE     �  CREATE TABLE "TempSchema"."Persona" (
    "TipoID" character varying(50),
    "PrimerNombre" character varying(20),
    "SegundoNombre" character varying(20),
    "PrimerApellido" character varying(50),
    "SegundoApellido" character varying(20),
    "Correo" character varying(50),
    "Telefono" bigint,
    "Año" integer,
    "IDUsuario" integer NOT NULL,
    "Identificacion" bigint NOT NULL
);
 #   DROP TABLE "TempSchema"."Persona";
    
   TempSchema         heap r       postgres    false    6            �            1259    16915    Persona_IDUsuario_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Persona_IDUsuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE "TempSchema"."Persona_IDUsuario_seq";
    
   TempSchema               postgres    false    232    6            p           0    0    Persona_IDUsuario_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE "TempSchema"."Persona_IDUsuario_seq" OWNED BY "TempSchema"."Persona"."IDUsuario";
       
   TempSchema               postgres    false    233            �            1259    16916    Persona_Identificacion_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Persona_Identificacion_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE "TempSchema"."Persona_Identificacion_seq";
    
   TempSchema               postgres    false    6    232            q           0    0    Persona_Identificacion_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE "TempSchema"."Persona_Identificacion_seq" OWNED BY "TempSchema"."Persona"."Identificacion";
       
   TempSchema               postgres    false    234            �            1259    16917    Usuario    TABLE     �   CREATE TABLE "TempSchema"."Usuario" (
    "IDUsuario" integer NOT NULL,
    "Rol" character varying(20),
    "Pwd" character varying,
    "Año" integer
);
 #   DROP TABLE "TempSchema"."Usuario";
    
   TempSchema         heap r       postgres    false    6            �            1259    16922    UsuarioTieneHorario    TABLE     v   CREATE TABLE "TempSchema"."UsuarioTieneHorario" (
    "CodigoH" integer NOT NULL,
    "IDUsuario" integer NOT NULL
);
 /   DROP TABLE "TempSchema"."UsuarioTieneHorario";
    
   TempSchema         heap r       postgres    false    6            �            1259    16925    UsuarioTieneHorario_CodigoH_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."UsuarioTieneHorario_CodigoH_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE "TempSchema"."UsuarioTieneHorario_CodigoH_seq";
    
   TempSchema               postgres    false    6    236            r           0    0    UsuarioTieneHorario_CodigoH_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE "TempSchema"."UsuarioTieneHorario_CodigoH_seq" OWNED BY "TempSchema"."UsuarioTieneHorario"."CodigoH";
       
   TempSchema               postgres    false    237            �            1259    16926 !   UsuarioTieneHorario_IDUsuario_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."UsuarioTieneHorario_IDUsuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE "TempSchema"."UsuarioTieneHorario_IDUsuario_seq";
    
   TempSchema               postgres    false    6    236            s           0    0 !   UsuarioTieneHorario_IDUsuario_seq    SEQUENCE OWNED BY     y   ALTER SEQUENCE "TempSchema"."UsuarioTieneHorario_IDUsuario_seq" OWNED BY "TempSchema"."UsuarioTieneHorario"."IDUsuario";
       
   TempSchema               postgres    false    238            �            1259    16927    Usuario_IDUsuario_seq    SEQUENCE     �   CREATE SEQUENCE "TempSchema"."Usuario_IDUsuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE "TempSchema"."Usuario_IDUsuario_seq";
    
   TempSchema               postgres    false    235    6            t           0    0    Usuario_IDUsuario_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE "TempSchema"."Usuario_IDUsuario_seq" OWNED BY "TempSchema"."Usuario"."IDUsuario";
       
   TempSchema               postgres    false    239            �           2604    16928 
   Aula Grupo    DEFAULT     z   ALTER TABLE ONLY "TempSchema"."Aula" ALTER COLUMN "Grupo" SET DEFAULT nextval('"TempSchema"."Aula_Grupo_seq"'::regclass);
 C   ALTER TABLE "TempSchema"."Aula" ALTER COLUMN "Grupo" DROP DEFAULT;
    
   TempSchema               postgres    false    221    220            �           2604    17081    Estudiante IDEstudiante    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Estudiante" ALTER COLUMN "IDEstudiante" SET DEFAULT nextval('"TempSchema"."Estudiante_IDEstudiante_seq"'::regclass);
 P   ALTER TABLE "TempSchema"."Estudiante" ALTER COLUMN "IDEstudiante" DROP DEFAULT;
    
   TempSchema               postgres    false    224    222            �           2604    16930    Examen IDEvaluacion    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Examen" ALTER COLUMN "IDEvaluacion" SET DEFAULT nextval('"TempSchema"."Examen_IDEvaluacion_seq"'::regclass);
 L   ALTER TABLE "TempSchema"."Examen" ALTER COLUMN "IDEvaluacion" DROP DEFAULT;
    
   TempSchema               postgres    false    226    225            �           2604    16931    Horario CodigoH    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Horario" ALTER COLUMN "CodigoH" SET DEFAULT nextval('"TempSchema"."Horario_CodigoH_seq"'::regclass);
 H   ALTER TABLE "TempSchema"."Horario" ALTER COLUMN "CodigoH" DROP DEFAULT;
    
   TempSchema               postgres    false    229    227            �           2604    16932    Institucion CodigoInsti    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Institucion" ALTER COLUMN "CodigoInsti" SET DEFAULT nextval('"TempSchema"."Institucion_CodigoInsti_seq"'::regclass);
 P   ALTER TABLE "TempSchema"."Institucion" ALTER COLUMN "CodigoInsti" DROP DEFAULT;
    
   TempSchema               postgres    false    231    230            �           2604    16933    Persona IDUsuario    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Persona" ALTER COLUMN "IDUsuario" SET DEFAULT nextval('"TempSchema"."Persona_IDUsuario_seq"'::regclass);
 J   ALTER TABLE "TempSchema"."Persona" ALTER COLUMN "IDUsuario" DROP DEFAULT;
    
   TempSchema               postgres    false    233    232            �           2604    17074    Persona Identificacion    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Persona" ALTER COLUMN "Identificacion" SET DEFAULT nextval('"TempSchema"."Persona_Identificacion_seq"'::regclass);
 O   ALTER TABLE "TempSchema"."Persona" ALTER COLUMN "Identificacion" DROP DEFAULT;
    
   TempSchema               postgres    false    234    232            �           2604    16935    Usuario IDUsuario    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."Usuario" ALTER COLUMN "IDUsuario" SET DEFAULT nextval('"TempSchema"."Usuario_IDUsuario_seq"'::regclass);
 J   ALTER TABLE "TempSchema"."Usuario" ALTER COLUMN "IDUsuario" DROP DEFAULT;
    
   TempSchema               postgres    false    239    235            �           2604    16936    UsuarioTieneHorario CodigoH    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario" ALTER COLUMN "CodigoH" SET DEFAULT nextval('"TempSchema"."UsuarioTieneHorario_CodigoH_seq"'::regclass);
 T   ALTER TABLE "TempSchema"."UsuarioTieneHorario" ALTER COLUMN "CodigoH" DROP DEFAULT;
    
   TempSchema               postgres    false    237    236            �           2604    16937    UsuarioTieneHorario IDUsuario    DEFAULT     �   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario" ALTER COLUMN "IDUsuario" SET DEFAULT nextval('"TempSchema"."UsuarioTieneHorario_IDUsuario_seq"'::regclass);
 V   ALTER TABLE "TempSchema"."UsuarioTieneHorario" ALTER COLUMN "IDUsuario" DROP DEFAULT;
    
   TempSchema               postgres    false    238    236            O          0    16870    AsistenciaEstudiante 
   TABLE DATA           d   COPY "TempSchema"."AsistenciaEstudiante" ("CodigoH", "IDEstudiante", "Fecha", "Asiste") FROM stdin;
 
   TempSchema               postgres    false    218          P          0    16874    AsistenciaUsuario 
   TABLE DATA           ^   COPY "TempSchema"."AsistenciaUsuario" ("CodigoH", "IDUsuario", "Fecha", "Asiste") FROM stdin;
 
   TempSchema               postgres    false    219   3       Q          0    16878    Aula 
   TABLE DATA           �   COPY "TempSchema"."Aula" ("Grupo", "GradoT", "GradoNum", "GrupoEquivalente", "Jornada", "Año", "CodigoInsti", "IDUsuario") FROM stdin;
 
   TempSchema               postgres    false    220   P       S          0    16884 
   Estudiante 
   TABLE DATA           �   COPY "TempSchema"."Estudiante" ("IDEstudiante", "TipoID", "PrimerNombre", "SegundoNombre", "PrimerApellido", "SegundoApellido", "Genero", "FechaNacimiento", "Estrato", "Año", "Grupo") FROM stdin;
 
   TempSchema               postgres    false    222   �       T          0    16889    EstudianteTieneHorario 
   TABLE DATA           S   COPY "TempSchema"."EstudianteTieneHorario" ("CodigoH", "IDEstudiante") FROM stdin;
 
   TempSchema               postgres    false    223   r�       V          0    16893    Examen 
   TABLE DATA           v   COPY "TempSchema"."Examen" ("IDEvaluacion", "Nota", "BloqueLectivo", "Año", "IDEstudiante", "IDUsuario") FROM stdin;
 
   TempSchema               postgres    false    225   �       X          0    16899    Horario 
   TABLE DATA           �   COPY "TempSchema"."Horario" ("CodigoH", "FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "DiaInicial", "DiaTexto") FROM stdin;
 
   TempSchema               postgres    false    227   c�       Y          0    16902    HorarioTieneAula 
   TABLE DATA           F   COPY "TempSchema"."HorarioTieneAula" ("CodigoH", "Grupo") FROM stdin;
 
   TempSchema               postgres    false    228   
�       [          0    16906    Institucion 
   TABLE DATA           �   COPY "TempSchema"."Institucion" ("CodigoInsti", "NombreInsti", "NombreRector", "Localidad", "Barrio", "Numero", "Direccion", "Año") FROM stdin;
 
   TempSchema               postgres    false    230   Y�       ]          0    16912    Persona 
   TABLE DATA           �   COPY "TempSchema"."Persona" ("TipoID", "PrimerNombre", "SegundoNombre", "PrimerApellido", "SegundoApellido", "Correo", "Telefono", "Año", "IDUsuario", "Identificacion") FROM stdin;
 
   TempSchema               postgres    false    232   A�       `          0    16917    Usuario 
   TABLE DATA           L   COPY "TempSchema"."Usuario" ("IDUsuario", "Rol", "Pwd", "Año") FROM stdin;
 
   TempSchema               postgres    false    235   ۡ       a          0    16922    UsuarioTieneHorario 
   TABLE DATA           M   COPY "TempSchema"."UsuarioTieneHorario" ("CodigoH", "IDUsuario") FROM stdin;
 
   TempSchema               postgres    false    236   Q�       u           0    0    Aula_Grupo_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('"TempSchema"."Aula_Grupo_seq"', 49, true);
       
   TempSchema               postgres    false    221            v           0    0    Estudiante_IDEstudiante_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('"TempSchema"."Estudiante_IDEstudiante_seq"', 118, true);
       
   TempSchema               postgres    false    224            w           0    0    Examen_IDEvaluacion_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('"TempSchema"."Examen_IDEvaluacion_seq"', 130, true);
       
   TempSchema               postgres    false    226            x           0    0    Horario_CodigoH_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('"TempSchema"."Horario_CodigoH_seq"', 60, true);
       
   TempSchema               postgres    false    229            y           0    0    Institucion_CodigoInsti_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('"TempSchema"."Institucion_CodigoInsti_seq"', 1, false);
       
   TempSchema               postgres    false    231            z           0    0    Persona_IDUsuario_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('"TempSchema"."Persona_IDUsuario_seq"', 1, false);
       
   TempSchema               postgres    false    233            {           0    0    Persona_Identificacion_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('"TempSchema"."Persona_Identificacion_seq"', 78, true);
       
   TempSchema               postgres    false    234            |           0    0    UsuarioTieneHorario_CodigoH_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('"TempSchema"."UsuarioTieneHorario_CodigoH_seq"', 1, false);
       
   TempSchema               postgres    false    237            }           0    0 !   UsuarioTieneHorario_IDUsuario_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('"TempSchema"."UsuarioTieneHorario_IDUsuario_seq"', 1, false);
       
   TempSchema               postgres    false    238            ~           0    0    Usuario_IDUsuario_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('"TempSchema"."Usuario_IDUsuario_seq"', 92, true);
       
   TempSchema               postgres    false    239            �           2606    16939    Horario Horario_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY "TempSchema"."Horario"
    ADD CONSTRAINT "Horario_pkey" PRIMARY KEY ("CodigoH");
 H   ALTER TABLE ONLY "TempSchema"."Horario" DROP CONSTRAINT "Horario_pkey";
    
   TempSchema                 postgres    false    227            �           2606    16941 -   AsistenciaEstudiante pk_asistencia_estudiante 
   CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante"
    ADD CONSTRAINT pk_asistencia_estudiante PRIMARY KEY ("CodigoH", "IDEstudiante", "Fecha");
 _   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante" DROP CONSTRAINT pk_asistencia_estudiante;
    
   TempSchema                 postgres    false    218    218    218            �           2606    16943 '   AsistenciaUsuario pk_asistencia_usuario 
   CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario"
    ADD CONSTRAINT pk_asistencia_usuario PRIMARY KEY ("CodigoH", "IDUsuario", "Fecha");
 Y   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario" DROP CONSTRAINT pk_asistencia_usuario;
    
   TempSchema                 postgres    false    219    219    219            �           2606    16945    Aula pk_id_aula 
   CONSTRAINT     Z   ALTER TABLE ONLY "TempSchema"."Aula"
    ADD CONSTRAINT pk_id_aula PRIMARY KEY ("Grupo");
 A   ALTER TABLE ONLY "TempSchema"."Aula" DROP CONSTRAINT pk_id_aula;
    
   TempSchema                 postgres    false    220            �           2606    17083    Estudiante pk_id_estudiante 
   CONSTRAINT     m   ALTER TABLE ONLY "TempSchema"."Estudiante"
    ADD CONSTRAINT pk_id_estudiante PRIMARY KEY ("IDEstudiante");
 M   ALTER TABLE ONLY "TempSchema"."Estudiante" DROP CONSTRAINT pk_id_estudiante;
    
   TempSchema                 postgres    false    222            �           2606    16949    Examen pk_id_examen 
   CONSTRAINT     e   ALTER TABLE ONLY "TempSchema"."Examen"
    ADD CONSTRAINT pk_id_examen PRIMARY KEY ("IDEvaluacion");
 E   ALTER TABLE ONLY "TempSchema"."Examen" DROP CONSTRAINT pk_id_examen;
    
   TempSchema                 postgres    false    225            �           2606    16951    Institucion pk_id_institucion 
   CONSTRAINT     n   ALTER TABLE ONLY "TempSchema"."Institucion"
    ADD CONSTRAINT pk_id_institucion PRIMARY KEY ("CodigoInsti");
 O   ALTER TABLE ONLY "TempSchema"."Institucion" DROP CONSTRAINT pk_id_institucion;
    
   TempSchema                 postgres    false    230            �           2606    17076    Persona pk_id_persona 
   CONSTRAINT     i   ALTER TABLE ONLY "TempSchema"."Persona"
    ADD CONSTRAINT pk_id_persona PRIMARY KEY ("Identificacion");
 G   ALTER TABLE ONLY "TempSchema"."Persona" DROP CONSTRAINT pk_id_persona;
    
   TempSchema                 postgres    false    232            �           2606    16955    Usuario pk_id_usuario 
   CONSTRAINT     d   ALTER TABLE ONLY "TempSchema"."Usuario"
    ADD CONSTRAINT pk_id_usuario PRIMARY KEY ("IDUsuario");
 G   ALTER TABLE ONLY "TempSchema"."Usuario" DROP CONSTRAINT pk_id_usuario;
    
   TempSchema                 postgres    false    235            �           2606    16957 5   EstudianteTieneHorario pk_relacion_estudiante_horario 
   CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."EstudianteTieneHorario"
    ADD CONSTRAINT pk_relacion_estudiante_horario PRIMARY KEY ("CodigoH", "IDEstudiante");
 g   ALTER TABLE ONLY "TempSchema"."EstudianteTieneHorario" DROP CONSTRAINT pk_relacion_estudiante_horario;
    
   TempSchema                 postgres    false    223    223            �           2606    16959 )   HorarioTieneAula pk_relacion_horario_aula 
   CONSTRAINT        ALTER TABLE ONLY "TempSchema"."HorarioTieneAula"
    ADD CONSTRAINT pk_relacion_horario_aula PRIMARY KEY ("CodigoH", "Grupo");
 [   ALTER TABLE ONLY "TempSchema"."HorarioTieneAula" DROP CONSTRAINT pk_relacion_horario_aula;
    
   TempSchema                 postgres    false    228    228            �           2606    16961 /   UsuarioTieneHorario pk_relacion_usuario_horario 
   CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario"
    ADD CONSTRAINT pk_relacion_usuario_horario PRIMARY KEY ("CodigoH", "IDUsuario");
 a   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario" DROP CONSTRAINT pk_relacion_usuario_horario;
    
   TempSchema                 postgres    false    236    236            �           2606    16962 &   AsistenciaEstudiante fk_codigo_horario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante"
    ADD CONSTRAINT fk_codigo_horario FOREIGN KEY ("CodigoH") REFERENCES "TempSchema"."Horario"("CodigoH") ON UPDATE CASCADE ON DELETE CASCADE;
 X   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante" DROP CONSTRAINT fk_codigo_horario;
    
   TempSchema               postgres    false    218    227    4774            �           2606    16967 #   AsistenciaUsuario fk_codigo_horario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario"
    ADD CONSTRAINT fk_codigo_horario FOREIGN KEY ("CodigoH") REFERENCES "TempSchema"."Horario"("CodigoH") ON UPDATE CASCADE ON DELETE CASCADE;
 U   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario" DROP CONSTRAINT fk_codigo_horario;
    
   TempSchema               postgres    false    4774    219    227            �           2606    17084    Examen fk_id_estudiante    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Examen"
    ADD CONSTRAINT fk_id_estudiante FOREIGN KEY ("IDEstudiante") REFERENCES "TempSchema"."Estudiante"("IDEstudiante");
 I   ALTER TABLE ONLY "TempSchema"."Examen" DROP CONSTRAINT fk_id_estudiante;
    
   TempSchema               postgres    false    225    4768    222            �           2606    17089 '   EstudianteTieneHorario fk_id_estudiante    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."EstudianteTieneHorario"
    ADD CONSTRAINT fk_id_estudiante FOREIGN KEY ("IDEstudiante") REFERENCES "TempSchema"."Estudiante"("IDEstudiante");
 Y   ALTER TABLE ONLY "TempSchema"."EstudianteTieneHorario" DROP CONSTRAINT fk_id_estudiante;
    
   TempSchema               postgres    false    222    223    4768            �           2606    17094 %   AsistenciaEstudiante fk_id_estudiante    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante"
    ADD CONSTRAINT fk_id_estudiante FOREIGN KEY ("IDEstudiante") REFERENCES "TempSchema"."Estudiante"("IDEstudiante") ON UPDATE CASCADE ON DELETE CASCADE;
 W   ALTER TABLE ONLY "TempSchema"."AsistenciaEstudiante" DROP CONSTRAINT fk_id_estudiante;
    
   TempSchema               postgres    false    222    218    4768            �           2606    16987    HorarioTieneAula fk_id_grupo    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."HorarioTieneAula"
    ADD CONSTRAINT fk_id_grupo FOREIGN KEY ("Grupo") REFERENCES "TempSchema"."Aula"("Grupo");
 N   ALTER TABLE ONLY "TempSchema"."HorarioTieneAula" DROP CONSTRAINT fk_id_grupo;
    
   TempSchema               postgres    false    220    4766    228            �           2606    16992    Estudiante fk_id_grupo    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Estudiante"
    ADD CONSTRAINT fk_id_grupo FOREIGN KEY ("Grupo") REFERENCES "TempSchema"."Aula"("Grupo");
 H   ALTER TABLE ONLY "TempSchema"."Estudiante" DROP CONSTRAINT fk_id_grupo;
    
   TempSchema               postgres    false    4766    220    222            �           2606    16997    Aula fk_id_institucion    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Aula"
    ADD CONSTRAINT fk_id_institucion FOREIGN KEY ("CodigoInsti") REFERENCES "TempSchema"."Institucion"("CodigoInsti");
 H   ALTER TABLE ONLY "TempSchema"."Aula" DROP CONSTRAINT fk_id_institucion;
    
   TempSchema               postgres    false    230    4778    220            �           2606    17002    Persona fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Persona"
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY ("IDUsuario") REFERENCES "TempSchema"."Usuario"("IDUsuario") NOT VALID;
 G   ALTER TABLE ONLY "TempSchema"."Persona" DROP CONSTRAINT fk_id_usuario;
    
   TempSchema               postgres    false    232    4782    235            �           2606    17007 !   UsuarioTieneHorario fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario"
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY ("IDUsuario") REFERENCES "TempSchema"."Usuario"("IDUsuario");
 S   ALTER TABLE ONLY "TempSchema"."UsuarioTieneHorario" DROP CONSTRAINT fk_id_usuario;
    
   TempSchema               postgres    false    4782    236    235            �           2606    17012    Examen fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Examen"
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY ("IDUsuario") REFERENCES "TempSchema"."Usuario"("IDUsuario");
 F   ALTER TABLE ONLY "TempSchema"."Examen" DROP CONSTRAINT fk_id_usuario;
    
   TempSchema               postgres    false    235    4782    225            �           2606    17017    AsistenciaUsuario fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario"
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY ("IDUsuario") REFERENCES "TempSchema"."Usuario"("IDUsuario") ON UPDATE CASCADE ON DELETE CASCADE;
 Q   ALTER TABLE ONLY "TempSchema"."AsistenciaUsuario" DROP CONSTRAINT fk_id_usuario;
    
   TempSchema               postgres    false    219    4782    235            �           2606    17022    Aula fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY "TempSchema"."Aula"
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY ("IDUsuario") REFERENCES "TempSchema"."Usuario"("IDUsuario") ON UPDATE CASCADE ON DELETE SET NULL;
 D   ALTER TABLE ONLY "TempSchema"."Aula" DROP CONSTRAINT fk_id_usuario;
    
   TempSchema               postgres    false    220    235    4782            O      x������ � �      P      x������ � �      Q   �   x�m�;�0E���b"�x(�iSD"]�PЀd��e�X�(����4Ǐ�!�C�aa<���0�0���Z�8�%�y����8b-�@�� ,1�g0�A�k8�FC��ʶ �\y�TČ�2Nk������]ֶ���W��Bi��Z����[+b� a��u�� {Z�y!�6ck      S   S  x�m�Mn�0���]T��dIˠ��qk�AW�010��@����z�^�3��GIÀ=s�{GmϞ����F�UM�����I_؃}���\�W�hX?d�jQtU;5Ŷz�xT�֞@�ۢL��-%g2��蜫�8���lF���:��%��ϔ(~Pˤ��������Ov��Ҭpn�꤫PG�m�`�5�0�'�n����Lʒ7���ik���f���AQ,�Y{�0,|�*��;=����A���p�w�z�s�(%Y����ݠ�Z�FÁ{e����^���0q2�)�U����6Gvs\�t��Ѿ�,cr
b��i;�[0j�'�I�`Fy������!����u)eT���G�Q�#d��ЁLx��ڲ��F�ژ%5�K�8)H;? /$�բR*�)��m���sP���MҨ>)" 2����	�Sϓ���co���t��3<m�j�R����t9y���$n��^=xY���J���m}�/@����5���}PQ�$�&� ,�s��{���W�s�?��"ʪBp��7uV�$�dm]%L�F�(t�=Kd�����J�^-�1Kƽ��uH�A�#�H��Qsn�tn��N�r��ڤK�������l�y��\?�M)����
Ѥ�V�T ��6�On�3 <R����_MKMv@���r������*(�ҵѐ��x���wԳ�6�Â�-��^e�v��������
�D�}q�F � �XgB��_\E��^����,
Fq���s���BhW�����ǰ�|<��[���>ӽ���Ю�~��?�1�vu����.��Fܦ�v�D�"��|��l��_����O�      T   h   x�%̻1Q[s�W�\6�8�ua�'�DO�*�����]ߚ$|�FaFQ�G��C��j�t������^Tk#���!����?�+q%}?"��&'�      V   i   x�E���@�73�1���ì[���>D�|ҭNQ�΢�l�s�&�R�!��Az�ŠO?�����\��z0�n�	�(T�b��͟ދ�m�&�      X   �  x�u��j�@����]R�1��
*�BiD
}�簨��3������|pc!�4�1�q�|5���������r�����K��eܷɆ���S����6�B�.��d�$/-�Ɏ���M��)�K�d�$/m�&��S�1j����X�& ��%,���#B"�E�@����6���"� �\��\�ru.B��EB่D�<���"!�n�v<\^�}UF*�_��Xe(C�l�6Da��qXe�C$V
�U�FDc����U�DDV*�sX>��B$B�WdDE�j "
�W(D<�
�G_���+�!}�:Ģ��P����+<,�WhC��i�z�f�QXr�K�?�"�4hB��E��Ҡ�W� �J��]iP��+�1�6#�6o]���`�      Y   ?   x�ʱ� ����^`zq�u����A�A��Đ��ͼ����sLjˋ<��u�7���Y      [      x��\���Fr����*%v�[�#sH�
 (��D����-۵�Co��j3��}?������� ���]Ә����?ȰC�"*�]{#j-t=V�jL'jh*%~Q(�6��sЭ8���5�W}��
:�_��sV}ЪAt�A����F��髱��V���R�����T�Q��t��BF��Q�J��gՊa�hܽ�������7W�� 	T��ش�
~#�>�������Q�Z��
��jE��$X�dH2D�K��	;��
�שׁ���L�:�;��������� r7�?�"NE�'-M��I�'��pm�# ŵ�a��y�+�V��C��� ����M'.
�����ǉ�D��;�j!����tAB�D�(R����y!�su����1{q���|0m}>����7�i?o�Ǧ}��s/�݌�	DYR���t���`��i;hT�5<xo�P��@Gi�^CBd�%�~}�ϞE{]�	l�����f�zדz��ژ႓��Yw��a`���
*���j���I�A$��"�׻���B����B��j�K�A�<�X����;H��0܇�[���,��b���"MD��8\kE��� ]�F�-�HAZV�V�G:�O�ze������LąPB�l���m�ĭ@(�� �<4�[�(��t���}^�H�W�I�"�^���C�o�`�x�CC���T'�[ujuǀe<Dr_����J����Æ<���=t`�$�S=��؛>������ڸ�ܰ& ����"�p ��eXlK0jl�PM���O�:_A�tl�]��$c��DLf��M4�lS�J��op����L��j�~�����'4t���⌉2��zϟ_��r�s�q%h��Eљ�>���$���>����t+=lǊ KNИJ�A졂̳={��%�o�c����;�W��Lg���P՟>����?2�XD	���2���X+2��ϱ�fT@> ��(��~�l<��)�o��H32(�����Ʀ�@��n��pLpQ�]t���|�yL�2j_�@b�@�)�b��X�x��47bW9;Xn-=�O;cю<o:�Z�ŷd�$*�jF�b�/y*������>խ���0L�M��ߙ
&^�
�Zi�CBQ��",�G�d{�w!�������<�O=|���9�N�M�@���{0� 썏�C$d@�#�t@i�M.�"@.��s34=QM�݇�-�����X�<�("�J���D�_<�)���E똰[�^i�<��d�Q��	��)���ˣ��AH8|���Q�â�rs��������N����Ձ<��JA�L�,��=�[|ɉR�� �
�<@�o0�!�j`���H��غx��MWG���(��h *�|���PҚ� ��P��C�<`�X�P�������X�xWph�=�,b����Dy���`��v����щ|[5�z\Ld�%���e�9�w�0bN#����Zm���A�j}PНm(<X�C F���ͱ��jV�e��Pwh$�ٷ�� �Zڡ[���d������j�#x+g�6�Qt������h�p KL���g}��1SS�;�e�V������P�/ �qⱀ]�8I�G�@���c�ա��
�n�1�T�p3z�&+�]j��㪫��`�@���IO�'7��_�����;ڠ<�]Y|Z�*q��N����q�²�f8+�Ҽ!�ł]?�mQi�?��?zx���u e�&`y	�x�͂1���Uq��(e\�&Tc;jY,�>n3� &�d�J/R��J��O���lۙ8NH�,*/��gMa�}���X>zK�X�`�1G���=�?+׻_�ɞ�?q
xqJiPB���/	'R����M
	�!�9�l��Ğ��#��=�сr�8��t���٨�hD����j�t^�s���r�X`���|*�t�w`s _�D� 1P�vhH*G��y(� �\\rd�3�9�h���̶���6d�Wx�)�A��ȱw���Iqi�A�v���E�y�0���YΗ��pjlߡ��Zh%p���3̝�M@����/I�'��dx����HT��Yu�x�]��#K��oxpJ�����se��v
`ٮEM�l��������0Yen�d����X&*e~��O~�m�F��^&�-���Y^�K�+��Bp�^������4)��5��E;),�F���+	؎ӕIJ�!��\��;W��OyY ��]���t�����ڄI���D����؆��%B��U�0ٶٶ��^^��S�����C$���	�ㅋ��e�V��8ԑ�ԑ?�,�7j-��4��dũ`�̖i���L���Q�M��m�� :��B@$�ӗ����RS��_���kg��):F��(rj.�����4��c�<�W�)��Mt+Zs> dK#
��T��"�lG"T��>`i,�8�¡�|d���5��r��"Ia�S�Y�#	LA/.�yо����
N8��D�fx�*���*=s�٣����a��9P�p==(ぜ�|"A�/��MTt�:!�������mz��kp�'���g!�<����o���2!K)B/���mK9R��y���/bܚ���р�e )0~�f�l)cdB����
�xG��hp��%f����L�������%e��Pv<~%����0����͒T�8�5�06���<�����wB8����7�w�ܓ���U�ةo��'�FT�
fI���j�4�n���F&"-D�i�8��E͔Y���uIk�E�7>�8���iO�!��f>�C�EQ���Ky��ێl��04]��#@�F�8q�w�z�[ S� ��yFǨ)ϡ$i����xN3����I����6�hq�z�o�ݙ��ݑ�'L�x�_ �U%:�+�"\Fx����0��%�JkC�d�z�}�"Wg���S�ϗ��q+v`���e܂z���g�v��¨�ѬxvEbC�rf1�R8"�Rp��ɟz	TE����T��� =��$�6�:�/�@�� 6%tq��FY��s�4�f �2p �,�|wE񃲖5\)��������(C]��I|/w�q[{f�����8I|0��̾H"d3�Z��iQ�#:�k��,�������H1��!j�^�d���r�ϡ����y�SD;�n�b&[9b��eU�Ϟ1W'罱�f�Scʬ�nx��$��� �a�����0e�o8U��Q7��ތ3�Y��(Z�QƾO�`�n���g
_��g�6����t�����1C��i����f�.@�Eux��9C)����4Ըܑ�x`Ӊ�i��S�g��%�hqж<��N&n����ۅ-^���7]8w�ι���)��o�/�H��4">�(*�L#���N����h�y
Z}��ߓ�O���>)�x
����m'���W+��E�v�D��[��TSPB�ߵk]|#gf��N�r}&y�۾�k�S�1e�n à��w}���9~/+%YA�ye�D�zz��)��9�G�����{��y�L�gq������乭�U�t�;�6 F�P�F�Am��Z�!zc��Ų��c�Qd
�LϿ���k�m������g�`w����饂�ta���1�y�B�l�uG�\U�"t��\�~���k!�E]�6�I�Gk(���ᖦ� ��a-�E�(^'��rG���ٗ����>�kn��pf�����"�Pm�azj+��T�P�v��ۘNAk�ܘ��>R[�KGNݡ�.�'��zC��`n���o�a
r�G���LG������"UZ���]F�H��NR}�/�f�a�詏�G|2����Y���#{Y�:r�= �~'َ\tK�Ia<N��nw�x�0�T:{�p_*2��+Bp�ዚqwȀ8l��/��R�Ul�W�|���<���5z��ܑ梥��28�*r΃�����Z��*��$��Vp@]�u��KNGPP���� �T"�S��A�~j{�s��ۈ�w
�t%'C�G��?�])`^�D�k=%ե� �	  �&N�	|)�wJK�2{ȹ�>%x�bG$��0���փI�zG��B��4� Y��J��BΈ�vAf{*��C�s�����q\e[]L\F�i�6(g��"��Q$j��ῆ����9�p=�B��˲�����:�'g�ѳ(�;쎻���G��͈�k+q�?z��L��բ�����R�G�F���s��he�������������t�}�%�n_�M���!5vY���O�ă-ʯ��:�(3W�s�C���ϣm�tVuϱ��e������<Pi�(���h���d粴�W<a(��Ra�POh�k�f�<��f)��"d{)�{��q���Q���D�,��eD���i��tL�.=^���6��N��d���(~n��`�}ߟ@=eS�B6�5/<-B�="��+E��� |X�����M���+Ql��ל
О׋e�W�g&w4�\��a��j�%��(Ȑ�/*��\NrFD�;����3�������dz�,՝���^�0�����'j����q�O�oI�0�v�/gu��u�}����3�1e��k��ޛ���R釷e���s#>� @����d���cn���N���-R�;_{�<J���<vT��@�%M��*s��V��M��9�b��nd�v|p��X����9��LsW~�,\�^+٦�]��ܐ����X��<(Ʀ�~G����x:8��(�Q��l��$)c%5�p	���Q��2,m�� j�	��=p�#����v��ओ*sP�����������)��������'&*�w�
�(�܀yc�{�u���47=�)����&�����Ɏ������Yޔ����#�t=��@ڙŘ��K�SZ�`�Vщpf�#�n0��x���� ���르Ӌ�ڒS���;�S�Y?�_��F�45S��XJWQ��1�ex�4�?�nl04U���c�I2u��hB�2z�#�N=b�GH�~%�{�z
��ͨ���24g�S&��)D����\g���G�ާ���@�뚗�5
�9f9ڒD쵆�2�V���Z�x4�<��4�Gy�+;koD(}k(� ��"#d*���lG�o�Ǜ�46��pՔ�m<�@��|"d�}�s
I�L s8JQyu�(�v�c[b�W8m�M}s�f�^�'��B���"�3�ɎI�A����sn�Z
��A	���h`<54�G�$�tyJ���^�8��y�X�Gn��F��G�Ғ�Z�jN%\�S��ea+�/� �m��epc��S[��Ú�À��/(��I#�#�瘋ފ|�됙�螅��zf�;1wU�A�rd�#)��>pE{vµ� ���3�~��^L.�	_(��L$)��S��{��U�;uG47L=Y<9���/�i����2�}&�#z��M��K��SSZ&8(��0H� H�@
o}�r���g,���k�KCS�fz� 5t �+��U����l�0�b�N>��1v�<����`�	�N��k�{�!Mj��!&�ґ�G�WHR���W�@�Ҿ�]�y�)D!`47Bi׷��c~���c2YIc:�K.͓`�;�V�n-E
>GHuZN��y�V��j}@vb��ty�SZ�k�'��$�;n�Ӹ�E��+�������R��]���@ ��/�vLg�*GvҐ�?�5���ÑP�����"��4���Da�g�z�^8����mA;��ᙘ�}A�+��U)j�����A�<�5�c�u��gZ�F�u��~;�I��Xf�����Ĭ^K���h�
�v_Ժm�̰H���oq��m��	�,+��g𧔼"�YO|ܖ$��x�@�[�f�vxFR����<��MsfD[��ڄ�Ǯu�eS�<C8���2Z6p����4QJ%��W��qD�DT�����#�=���t� �h���JkJ�5����u�3�d�|�0���e)����T3��ug�jX��x/W�N>�_G�'�Q����~�uj��kjFu��A����U�:��͋�T�'��= g�#�1I��d)V9�A�d�"qV��	Y�w�Y+�Cą^�8�v�Ijd�ir;��;,�S�uXm�w���I3����_%;2��՟���6&�;��n�P��Zx�M�fo܄�&I�e��͏�;2�VbFt7I�	&Y�x;�����St�&��]�-�N�Ӥ�¸Ǫ�OD˄YpQ P�_4 ����e�֝�GΧ��)�dYGЌ`�� ��2��'ig���~���}G��z����TM?g��V՟��$w�����Q���2I�Zٰ�T���,��u��5Z_��N��kT菝_"u�C�J�D* M�ɮ�¥���$��O&4�-��2)�xǎ��f��/m-��@�6A�M��3��48���Ǟ��3Pm�s��|�[��_.��4�X�NQ��d�s?��{��^����sx}���z��� ����t5V�H�ݸ���JpWù�$�w����=��t��L�>R�$ʅa�۷~������K      ]   �  x�m�KN�0���0V���U���� Vl��T�;r�.r#���'�HlRg~��d�n�l�S�6荫����U{W��L���T�ڈ�M&�4�g���4�e��\M�MO>��[�-Z��s%q�F�P�D�Ba���hќ(���ҫ:lqі؝�-Z].J�<k�� �������:?b��ޜ{�	��.3��!���r�[et��#�w�C_�>�e��c���|��Vk�T&�ߝϜVu��	ձ��K���6�Rk�ΡC/4�6N��b�BqL���
�<�{�Z��=�џ��R��Kd�kW��8wt�k��E�UKx�z�������
�c�%����zmi�M82��Nz}jh�����H?�Uz��$"I�_�:�      `   f   x�u�;� EњY���P�K
?A��㘩,߹�C#��mU�WVBKm-�&rL��3Y��䈐�E��R�L����Ę����Ք{J��N��:=� ��^<�      a   =   x�˱�0�Z&g8x��?G��F��)6���6*�K����z���8��:��C����     