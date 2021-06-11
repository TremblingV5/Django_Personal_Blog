# compose/mysql/init/init.sql
-- Alter user 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
-- GRANT ALL PRIVILEGES ON personal_blog.* TO 'admin'@'%';
-- FLUSH PRIVILEGES;
/*
 Navicat Premium Data Transfer

 Source Server         : Localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : personal_blog

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 13/05/2021 23:30:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for articles_articlecategories
-- ----------------------------
DROP TABLE IF EXISTS `articles_articlecategories`;
CREATE TABLE `articles_articlecategories`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for articles_articles
-- ----------------------------
DROP TABLE IF EXISTS `articles_articles`;
CREATE TABLE `articles_articles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `introduction` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `coverImage` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `cate_id_id` int(11) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `in_turn` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `articles_articles_cate_id_id_12a963a4`(`cate_id_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissions_group_id_b120cbf9`(`group_id`) USING BTREE,
  INDEX `auth_group_permissions_permission_id_84c5c92e`(`permission_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  INDEX `auth_permission_content_type_id_2f476e4b`(`content_type_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 73 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add article categories', 7, 'add_articlecategories');
INSERT INTO `auth_permission` VALUES (26, 'Can change article categories', 7, 'change_articlecategories');
INSERT INTO `auth_permission` VALUES (27, 'Can delete article categories', 7, 'delete_articlecategories');
INSERT INTO `auth_permission` VALUES (28, 'Can view article categories', 7, 'view_articlecategories');
INSERT INTO `auth_permission` VALUES (29, 'Can add articles', 8, 'add_articles');
INSERT INTO `auth_permission` VALUES (30, 'Can change articles', 8, 'change_articles');
INSERT INTO `auth_permission` VALUES (31, 'Can delete articles', 8, 'delete_articles');
INSERT INTO `auth_permission` VALUES (32, 'Can view articles', 8, 'view_articles');
INSERT INTO `auth_permission` VALUES (33, 'Can add about me', 9, 'add_aboutme');
INSERT INTO `auth_permission` VALUES (34, 'Can change about me', 9, 'change_aboutme');
INSERT INTO `auth_permission` VALUES (35, 'Can delete about me', 9, 'delete_aboutme');
INSERT INTO `auth_permission` VALUES (36, 'Can view about me', 9, 'view_aboutme');
INSERT INTO `auth_permission` VALUES (37, 'Can add represent articles', 10, 'add_representarticles');
INSERT INTO `auth_permission` VALUES (38, 'Can change represent articles', 10, 'change_representarticles');
INSERT INTO `auth_permission` VALUES (39, 'Can delete represent articles', 10, 'delete_representarticles');
INSERT INTO `auth_permission` VALUES (40, 'Can view represent articles', 10, 'view_representarticles');
INSERT INTO `auth_permission` VALUES (41, 'Can add carousel', 11, 'add_carousel');
INSERT INTO `auth_permission` VALUES (42, 'Can change carousel', 11, 'change_carousel');
INSERT INTO `auth_permission` VALUES (43, 'Can delete carousel', 11, 'delete_carousel');
INSERT INTO `auth_permission` VALUES (44, 'Can view carousel', 11, 'view_carousel');
INSERT INTO `auth_permission` VALUES (45, 'Can add capability stack', 12, 'add_capabilitystack');
INSERT INTO `auth_permission` VALUES (46, 'Can change capability stack', 12, 'change_capabilitystack');
INSERT INTO `auth_permission` VALUES (47, 'Can delete capability stack', 12, 'delete_capabilitystack');
INSERT INTO `auth_permission` VALUES (48, 'Can view capability stack', 12, 'view_capabilitystack');
INSERT INTO `auth_permission` VALUES (49, 'Can add external sites', 13, 'add_externalsites');
INSERT INTO `auth_permission` VALUES (50, 'Can change external sites', 13, 'change_externalsites');
INSERT INTO `auth_permission` VALUES (51, 'Can delete external sites', 13, 'delete_externalsites');
INSERT INTO `auth_permission` VALUES (52, 'Can view external sites', 13, 'view_externalsites');
INSERT INTO `auth_permission` VALUES (53, 'Can add projects', 14, 'add_projects');
INSERT INTO `auth_permission` VALUES (54, 'Can change projects', 14, 'change_projects');
INSERT INTO `auth_permission` VALUES (55, 'Can delete projects', 14, 'delete_projects');
INSERT INTO `auth_permission` VALUES (56, 'Can view projects', 14, 'view_projects');
INSERT INTO `auth_permission` VALUES (57, 'Can add resume', 15, 'add_resume');
INSERT INTO `auth_permission` VALUES (58, 'Can change resume', 15, 'change_resume');
INSERT INTO `auth_permission` VALUES (59, 'Can delete resume', 15, 'delete_resume');
INSERT INTO `auth_permission` VALUES (60, 'Can view resume', 15, 'view_resume');
INSERT INTO `auth_permission` VALUES (61, 'Can add basic info', 16, 'add_basicinfo');
INSERT INTO `auth_permission` VALUES (62, 'Can change basic info', 16, 'change_basicinfo');
INSERT INTO `auth_permission` VALUES (63, 'Can delete basic info', 16, 'delete_basicinfo');
INSERT INTO `auth_permission` VALUES (64, 'Can view basic info', 16, 'view_basicinfo');
INSERT INTO `auth_permission` VALUES (65, 'Can add admin user', 17, 'add_adminuser');
INSERT INTO `auth_permission` VALUES (66, 'Can change admin user', 17, 'change_adminuser');
INSERT INTO `auth_permission` VALUES (67, 'Can delete admin user', 17, 'delete_adminuser');
INSERT INTO `auth_permission` VALUES (68, 'Can view admin user', 17, 'view_adminuser');
INSERT INTO `auth_permission` VALUES (69, 'Can add contact info', 18, 'add_contactinfo');
INSERT INTO `auth_permission` VALUES (70, 'Can change contact info', 18, 'change_contactinfo');
INSERT INTO `auth_permission` VALUES (71, 'Can delete contact info', 18, 'delete_contactinfo');
INSERT INTO `auth_permission` VALUES (72, 'Can view contact info', 18, 'view_contactinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_user_id_6a12ed8b`(`user_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544`(`group_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permissions_user_id_a95ead1b`(`user_id`) USING BTREE,
  INDEX `auth_user_user_permissions_permission_id_1fbb5f2c`(`permission_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for blog_aboutme
-- ----------------------------
DROP TABLE IF EXISTS `blog_aboutme`;
CREATE TABLE `blog_aboutme`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_aboutme
-- ----------------------------
INSERT INTO `blog_aboutme` VALUES (1, 'Test', 1, 0, '2021-05-13 23:29:41.000000', '2021-05-13 23:29:45.000000');

-- ----------------------------
-- Table structure for blog_carousel
-- ----------------------------
DROP TABLE IF EXISTS `blog_carousel`;
CREATE TABLE `blog_carousel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sort` int(11) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `article_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `blog_carousel_article_id_id_dee427f6`(`article_id_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for blog_representarticles
-- ----------------------------
DROP TABLE IF EXISTS `blog_representarticles`;
CREATE TABLE `blog_representarticles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sort` int(11) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `article_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `blog_representarticles_article_id_id_c5ba0f16`(`article_id_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6`(`user_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'articles', 'articlecategories');
INSERT INTO `django_content_type` VALUES (8, 'articles', 'articles');
INSERT INTO `django_content_type` VALUES (9, 'blog', 'aboutme');
INSERT INTO `django_content_type` VALUES (10, 'blog', 'representarticles');
INSERT INTO `django_content_type` VALUES (11, 'blog', 'carousel');
INSERT INTO `django_content_type` VALUES (12, 'resume', 'capabilitystack');
INSERT INTO `django_content_type` VALUES (13, 'resume', 'externalsites');
INSERT INTO `django_content_type` VALUES (14, 'resume', 'projects');
INSERT INTO `django_content_type` VALUES (15, 'resume', 'resume');
INSERT INTO `django_content_type` VALUES (16, 'resume', 'basicinfo');
INSERT INTO `django_content_type` VALUES (17, 'manager', 'adminuser');
INSERT INTO `django_content_type` VALUES (18, 'manager', 'contactinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-04-19 06:50:05.015288');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-04-19 06:50:05.198264');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-04-19 06:50:05.243667');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-04-19 06:50:05.250498');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-19 06:50:05.258306');
INSERT INTO `django_migrations` VALUES (6, 'articles', '0001_initial', '2021-04-19 06:50:05.295394');
INSERT INTO `django_migrations` VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2021-04-19 06:50:05.329089');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2021-04-19 06:50:05.344704');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2021-04-19 06:50:05.359345');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2021-04-19 06:50:05.367152');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2021-04-19 06:50:05.383744');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2021-04-19 06:50:05.386672');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2021-04-19 06:50:05.394480');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2021-04-19 06:50:05.408144');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2021-04-19 06:50:05.423760');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2021-04-19 06:50:05.439375');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2021-04-19 06:50:05.450112');
INSERT INTO `django_migrations` VALUES (18, 'auth', '0012_alter_user_first_name_max_length', '2021-04-19 06:50:05.464751');
INSERT INTO `django_migrations` VALUES (19, 'blog', '0001_initial', '2021-04-19 06:50:05.528928');
INSERT INTO `django_migrations` VALUES (20, 'resume', '0001_initial', '2021-04-19 06:50:05.582607');
INSERT INTO `django_migrations` VALUES (21, 'resume', '0002_basicinfo', '2021-04-19 06:50:05.602128');
INSERT INTO `django_migrations` VALUES (22, 'sessions', '0001_initial', '2021-04-19 06:50:05.621647');
INSERT INTO `django_migrations` VALUES (23, 'resume', '0003_alter_resume_title', '2021-04-19 08:50:57.665782');
INSERT INTO `django_migrations` VALUES (24, 'manager', '0001_initial', '2021-04-20 06:09:04.561616');
INSERT INTO `django_migrations` VALUES (25, 'resume', '0004_alter_basicinfo_email', '2021-04-22 04:38:00.834985');
INSERT INTO `django_migrations` VALUES (26, 'blog', '0002_alter_aboutme_content', '2021-04-22 14:47:22.102663');
INSERT INTO `django_migrations` VALUES (27, 'resume', '0005_alter_resume_type', '2021-04-23 01:42:26.693590');
INSERT INTO `django_migrations` VALUES (28, 'articles', '0002_articlecategories_is_using', '2021-04-23 05:22:12.809295');
INSERT INTO `django_migrations` VALUES (29, 'articles', '0003_alter_articles_content', '2021-04-23 05:43:53.303137');
INSERT INTO `django_migrations` VALUES (30, 'articles', '0004_articles_is_using', '2021-04-23 06:29:22.373192');
INSERT INTO `django_migrations` VALUES (31, 'articles', '0005_alter_articles_coverimage', '2021-04-23 06:46:42.044827');
INSERT INTO `django_migrations` VALUES (32, 'articles', '0006_alter_articles_coverimage', '2021-04-23 12:55:07.348292');
INSERT INTO `django_migrations` VALUES (33, 'articles', '0007_alter_articles_coverimage', '2021-04-23 12:55:56.326317');
INSERT INTO `django_migrations` VALUES (34, 'articles', '0008_alter_articles_coverimage', '2021-04-23 12:57:37.675289');
INSERT INTO `django_migrations` VALUES (35, 'articles', '0009_alter_articles_coverimage', '2021-04-23 13:03:29.906119');
INSERT INTO `django_migrations` VALUES (36, 'articles', '0010_alter_articles_coverimage', '2021-04-23 13:13:05.752375');
INSERT INTO `django_migrations` VALUES (37, 'articles', '0011_alter_articles_coverimage', '2021-04-23 13:13:31.419219');
INSERT INTO `django_migrations` VALUES (38, 'articles', '0012_alter_articles_coverimage', '2021-04-23 13:13:49.772011');
INSERT INTO `django_migrations` VALUES (39, 'articles', '0013_alter_articles_coverimage', '2021-04-23 13:20:23.217082');
INSERT INTO `django_migrations` VALUES (40, 'articles', '0014_auto_20210424_0117', '2021-04-23 17:17:28.228535');
INSERT INTO `django_migrations` VALUES (41, 'articles', '0015_alter_articles_coverimage', '2021-04-23 17:21:33.450352');
INSERT INTO `django_migrations` VALUES (42, 'manager', '0002_contactinfo', '2021-04-24 02:35:04.105883');
INSERT INTO `django_migrations` VALUES (43, 'articles', '0016_alter_articles_coverimage', '2021-04-28 09:39:17.587940');
INSERT INTO `django_migrations` VALUES (44, 'resume', '0006_auto_20210501_1707', '2021-05-01 09:08:01.048716');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for manager_adminuser
-- ----------------------------
DROP TABLE IF EXISTS `manager_adminuser`;
CREATE TABLE `manager_adminuser`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `mobile` varchar(13) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of manager_adminuser
-- ----------------------------
INSERT INTO `manager_adminuser` VALUES (2, 'admin', '63a9f0ea7bb98050796b649e85481845', 'test', '13355556666', 'test@test.com');

-- ----------------------------
-- Table structure for manager_contactinfo
-- ----------------------------
DROP TABLE IF EXISTS `manager_contactinfo`;
CREATE TABLE `manager_contactinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `message` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_viewed` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resume_basicinfo
-- ----------------------------
DROP TABLE IF EXISTS `resume_basicinfo`;
CREATE TABLE `resume_basicinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `introduction` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `birthday` date NOT NULL,
  `mobile` varchar(13) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `website` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `address` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `personalImage` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `personalQRCode` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `vCard` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resume_basicinfo
-- ----------------------------
INSERT INTO `resume_basicinfo` VALUES (5, 'Test', '家里蹲', '我就是万能的Test', '2021-05-01', '13566554655', '123@123.com', 'http://www.baidu.com', '美国白宫', 1, 0, '2021-05-13 05:58:19.499607', '2021-05-13 05:58:19.499607', '', '', '');

-- ----------------------------
-- Table structure for resume_capabilitystack
-- ----------------------------
DROP TABLE IF EXISTS `resume_capabilitystack`;
CREATE TABLE `resume_capabilitystack`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `rate` int(11) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resume_externalsites
-- ----------------------------
DROP TABLE IF EXISTS `resume_externalsites`;
CREATE TABLE `resume_externalsites`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `icon` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `icon_selected` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resume_projects
-- ----------------------------
DROP TABLE IF EXISTS `resume_projects`;
CREATE TABLE `resume_projects`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `introductions` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `url` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `online_url` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for resume_resume
-- ----------------------------
DROP TABLE IF EXISTS `resume_resume`;
CREATE TABLE `resume_resume`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `introduction` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NOT NULL,
  `is_now` tinyint(1) NOT NULL,
  `type` varchar(3) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
