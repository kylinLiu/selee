from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# key = 'Af7ugPbk3UvU2WU2Y37xww27nyWak2Dj'
# data = 'UoFUtoiCnMzs+HkE8DmhOzaeGjZzY0xyr/j1halLTrM='
# # data = 'UoFUtoiCnMzs+HkE8DmhOzaeGjZzY0xyr/j1halLTrM='
# # data = '1693039605-1693039605'
# data = '1693090946-1693090946'
import base64
import urllib.parse


def pad(data):
    text = data + chr(16 - len(data) % 16) * (16 - len(data) % 16)
    return text


def unpad(s):
    last_num = s[-1]
    text = s[:-last_num]
    return text


def aes_ECB_Decrypt(data, key):  # ECB模式的解密函数，data为密文，key为16字节密钥
    key = key.encode('utf-8')
    aes = AES.new(key=key, mode=AES.MODE_ECB)  # 创建解密对象

    # decrypt AES解密  B64decode为base64 转码
    result = aes.decrypt(base64.b64decode(data))
    result = unpad(result)  # 除去补16字节的多余字符
    xx = str(result, 'utf-8')
    xx = urllib.parse.quote(xx)
    return xx # 以字符串的形式返回


def aes_ECB_Encrypt(data, key):  # ECB模式的加密函数，data为明文，key为16字节密钥
    key = key.encode('utf-8')
    data = pad(data)  # 补位
    data = data.encode('utf-8')
    aes = AES.new(key=key, mode=AES.MODE_ECB)  # 创建加密对象
    # encrypt AES加密  B64encode为base64转二进制编码
    result = base64.b64encode(aes.encrypt(data))
    xx = str(result, 'utf-8')
    xx = urllib.parse.quote(xx)
    return xx  # 以字符串的形式返回


# print(aes_ECB_Decrypt(data, key))
# print(aes_ECB_Encrypt(data, key))
"""

CREATE TABLE `dp_times` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `areaId` int NOT NULL COMMENT '景区id',
  `activityName` varchar(16) DEFAULT NULL COMMENT '景区名称',
  `activityDate` varchar(16) NOT NULL COMMENT '日期',
  `activityId` int DEFAULT NULL COMMENT '日期id',
  `timeId` int DEFAULT NULL COMMENT '时间id',
  `timeStr` varchar(64) NOT NULL COMMENT '时间段',
  `isvalid` tinyint DEFAULT '1' COMMENT '有效',
  `create_time` bigint NOT NULL COMMENT '创建时间',
  `update_time` bigint NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_areaId_activityDate_timeStr` (`areaId`,`activityDate`,`timeStr`),
  KEY `idx_activityDate` (`activityDate`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_update_time` (`update_time`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC COMMENT='dp时间参数表';


CREATE TABLE `dp_order` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `order_id` varchar(256) DEFAULT NULL COMMENT '订单id',
  `username` varchar(256) DEFAULT NULL COMMENT '用户名',
  `mobile` bigint DEFAULT '1' COMMENT '手机号',
  `sms` int DEFAULT NULL COMMENT '验证码',
  `plateNum` varchar(32) DEFAULT NULL COMMENT '车牌',
  `plateType` varchar(32) DEFAULT NULL COMMENT '车牌类型',
  `plateTypeStr` varchar(32) DEFAULT NULL COMMENT '车牌类型描述',
  `areaId` int DEFAULT NULL COMMENT '景区id',
  `jqName` varchar(16) DEFAULT NULL COMMENT '景区名称',
  `token` varchar(128) DEFAULT NULL COMMENT 'token',
  `activityDate` varchar(16) NOT NULL COMMENT '日期',
  `timeId` int DEFAULT NULL COMMENT '时间段ID',
  `order_status` tinyint DEFAULT '0' COMMENT '工单状态（-1:取消,0:新建,1:请求运行,2:运行中,3:请求暂停,4:已暂停,5:报错,6:完成,7:成功,8:失败,9:发货）',
  `timeStr` varchar(64) DEFAULT NULL COMMENT '时间段',
  `message` varchar(512) DEFAULT NULL COMMENT '报错信息',
  `inner_req_b` varchar(2048) DEFAULT NULL COMMENT '内部请求体',
  `outer_req_u` varchar(2048) DEFAULT NULL COMMENT '外部请求地址',
  `outer_req_h` varchar(2048) DEFAULT NULL COMMENT '外部请求头',
  `outer_req_b` varchar(2048) DEFAULT NULL COMMENT '外部请求体',
  `outer_res_b` varchar(2048) DEFAULT NULL COMMENT '外部响应体',
  `create_time` bigint NOT NULL COMMENT '创建时间',
  `update_time` bigint NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_order_id` (`order_id`),
  KEY `idx_username` (`username`),
  KEY `idx_mobile` (`mobile`),
  KEY `idx_activityDate` (`activityDate`),
  KEY `idx_jq_activityDate_timeId` (`areaId`,`activityDate`,`timeId`),
  KEY `idx_jq_activityDate_timeStr` (`areaId`,`activityDate`,`timeStr`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_update_time` (`update_time`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC COMMENT='dp工单表';


CREATE TABLE `dp_mobile` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `mobile` bigint NOT NULL COMMENT '手机号',
  `sms` int DEFAULT NULL COMMENT '验证码',
  `token` varchar(128) DEFAULT NULL COMMENT 'token',
  `username` varchar(256) DEFAULT NULL COMMENT '用户名',
  `create_time` bigint NOT NULL COMMENT '创建时间',
  `update_time` bigint NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_mobile` (`mobile`),
  KEY `idx_username` (`username`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_update_time` (`update_time`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC COMMENT='dp手机表';




INSERT INTO `kzz`.`dp_order`(`id`, `order_id`, `username`, `mobile`, `sms`, `plateNum`, `plateType`, `plateTypeStr`, `areaId`, `jqName`, `token`, `activityDate`, `timeId`, `order_status`, `timeStr`, `message`, `inner_req_b`, `outer_req_u`, `outer_req_h`, `outer_req_b`, `outer_res_b`, `create_time`, `update_time`) VALUES (136, '', '', 13691989775, NULL, '粤BBD9812', '', '普通车牌', 104, '仙湖植物园停车场', NULL, '2023-08-26', NULL, 0, '00:00-24:00', NULL, '{\"mobile\": \"13691989775\", \"sms\": \"\", \"plateNum\": \"\", \"plateType\": \"\", \"areaId\": 104, \"activityDate\": \"2023-08-26\", \"timeStr\": \"00:00-24:00\", \"username\": \"\", \"order_id\": \"\"}', NULL, NULL, NULL, NULL, 1692883179824, 1692883179824);

"""
