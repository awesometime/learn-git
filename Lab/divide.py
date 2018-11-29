#### 将一个大表格groupby后分成几个子表格

import pandas as pd

col_name = "EventID,ReceiveTime,OccurTime,RecentTime,ReporterID,ReporterIP,EventSrcIP,EventSrcName,EventSrcCategory,EventSrcType,EventType,EventName,EventDigest,EventLevel,SrcIP,SrcPort,DestIP,DestPort,NatSrcIP,NatSrcPort,NatDestIP,NatDestPort,SrcMac,DestMac,Duration,UpBytes,DownBytes,Protocol,AppProtocol,UserName,OperType,OperResult,ObjectName,Reponse,MergeCount,ProgramName,RequestContent,Action,DestServiceName,DestHostName,DestUserPrivileges,DestProcessName,DestUserId,DestUserAccount,ExternalID,FileCreateTime,FileModifyTime,FilePath,FilePermission,OldFileCreateTime,OldFileMD5,OldFileModifyTime,OldFileName,OldFilePath,OldFilePermission,OldFileType,RequestMethod,SrcHostName,SrcServiceName,SrcUserPrivileges,SrcProcessName,SrcUserId,SrcUserAccount,OriginalData,ThreatLevel,OnThreatIP,EventCategory,RuleID,OriEventID,OriMetaDataID,ConfidenceLevel,ParentThreatExist,AtkDirection,DomainName,DestIPRange,DestPortRange,DataOutSendType,FileDownType,FileName,FileType,FileMD5,Reputation,URL,HttpRefer,HttpUserAgent,URLCategory,MailReceivers,MailSender,MailID,SrcArea,DestArea,SrcIPUser,DestIPUser,SrcGeographyLocationCountryOrRegion,SrcGeographyLocationCity,SrcGeographyLocationLongitude,SrcGeographyLocationLatitude,DestGeographyLocationCountryOrRegion,DestGeographyLocationCity,DestGeographyLocationLongitude,DestGeographyLocationLatitude,ReceiveDate,OriEventType,MailSubject,MailAbstract,MailReader,MailServerName,MailServerIP,FileSize,FileDirection,ConnectPeriod,SignatureID,DomainIP,SrcHostUniqueID,DstHostUniqueID,OnThreatHost,SubmitTime,SubmitIP,ParentMd5,IsUnited,SubmitSource,AppType,PolicyName,PolicyId,SubAppType,VFWName,VirusFamily,VirusPlatform,VirusType,VirusName,ProfileName,IPSEventCategory,threatName,btwType,EventSubType,SystemCommand,SrcProcessID,DestProcessID,AccountName,AccountGroupID,AccountGroupName,TransactionTag,CurrentDir,AuditKey,HitCount,ProtectObject,AttackStatus,DropPackets,DropKbits,TenantID,DataType,EventClass,DetectType,OS,CveID,BotnetRole,MailSendTime,FileSha1,FileSha256,UrlMD5,FileSubType,IsThreatDecision,AttackPhase,ESN,ThreatScore,ReportSHA256,IsDnsServer,LocalVulID,VulID,VulName,VulScanTargets,VulPort,MessString,VulType,VulScanTaskID,PluginID,VulCategory,RiskPoints,VulDescription,VulSolution,ScanTaskStartTime,ScanTaskEndTime,ScanTaskType,ProductName,ProductVersion,VulLibVersion,Vendor,OriVulScanEventID,SourceType,SourceID,AlarmCategory,OriginalEventSrcIP,AffectedRows,ErrorMessage,ErrorID,DetectResult,ForensicsData,GroupID,DataCenterId,DataCenterName,ScopeId,ScopeLabel,ScopeName,AssetType,AssetHostName,AssetDetectResult,AssetThreatScore,AssetIP,AssetAttackType,AssetWorth,AssetUpdateTime,AttackEvidenceID,Standby022,Standby023,Standby024,Standby025,Standby026,Standby027,Standby028,Standby029,Standby030,Standby031,Standby032,Standby033,Standby034,Standby035,Standby036,Standby037,Standby038,Standby039,Standby040,Standby041,Standby042,Standby043,Standby044,Standby045,Standby046,Standby047,Standby048,Standby049,Standby050,Standby051,Standby052,Standby053,Standby054,Standby055,Standby056,Standby057,Standby058,Standby059,Standby060,ack_pps,app_proto,attack_type,authentication_info,biz_id,bps,bytes_tcp,bytes_toc,bytes_tos,bytes_udp,close_session,count,dest_ip_int,deszname,dip,dns_reply_kbps,dns_reply_pps,dns_request_kbps,dns_request_pps,end_time,est_session,eventtime ,finrst_pps,flow_est,flow_new,flow_reason,forward,http_get_pps,http_kbps,http_pps,https_kbps,https_pps,icmp_kbps,icmp_pps,iplocation_id,is_deszone,is_iplocation,log_time,new_session,other_kbps,other_pps,phyport,pkts_tcp,pkts_toc,pkts_toc_1024,pkts_toc_128,pkts_toc_1514,pkts_toc_256,pkts_toc_384,pkts_toc_512,pkts_toc_63,pkts_toc_640,pkts_toc_768,pkts_toc_896,pkts_toc_more,pkts_tos,pkts_tos_1024,pkts_tos_128,pkts_tos_1514,pkts_tos_256,pkts_tos_384,pkts_tos_512,pkts_tos_63,pkts_tos_640,pkts_tos_768,pkts_tos_896,pkts_tos_more,pkts_udp,plyuid,pps,protocol,recursion_info,req_len,res_len,resolution_info,resolution_result,response_code,sequence_number,serial_id,signname,signnum,signuid,sip,sip_invite_kbps,sip_invite_pps,src_ip,srczname,start_time_alert,start_time_attack,status,syn_pps,syn_pps_todeleted,synack_pps,syslog_category,tcp_flags,tcp_fragkbps,tcp_fragpps,tcp_kbps,tcp_pps,tcp_state,tcp_stream,tcp_toc_flags,tcp_tos_flags,threshold,tipid,total_kbps,total_pps,type,udp_fragkbps,udp_fragpps,udp_kbps,udp_pps,url_n,vlanid,xtime,xtime_us,zone_id,alarm_status,alarm_type,alert_time,alert_timestamp,alertname,attack_type_,begin_time,category,client_ip,createtime,curr_conn,destination_vpn_id,displayname,divert_ip,drop_kbps,drop_pps,dstip,hostname,icmp_concur_con,icmp_increase_con,immediateaction,in_kbps,in_pps,log_type,max_in_kbps,max_in_pps,max_severity,new_conn,other_concur_con,other_increase_con,querystring,responsecode,responsesize,responsetime,service_type,severgroupname,severity,signature_name,source_vpn_id,SrcIPInfo,syslog_id,sysname,tcp_concur_con,tcp_increase_con,time,udp_concur_con,udp_increase_con,urlhost,vgname,virtual_ip,vsys_name,RuleName,ccode,ipwhere,SrcHostType,DestHostType,SrcDestConn,SrcDestConnDay,SrcDestUseDay,srep,drep,SrcConn,SrcConDay,SrcUseDay,DestConn,DestUseDay,DestConnDay,flags,msize,muti_size,capfile,device_name,IPID,PORTID,payload,last_time,ipver,stored_info,deviceEventClassID,event_number,updateTime,attacked_service,ApplicationName,soapAction,sessionID,additionalUserName,webCorre,queryparamName,queryparamValue,queryheadersName,queryheadersValue,ddName"
col_name = col_name.split(",")
# print(type(col_name))  # list
# print(len(col_name))   460

# 将csv文件转化成DataFrame格式
demo_df = pd.read_csv('F:\\hw_data\\log\\MoBwJHArSJudj56qedp.dis-pck-antiddos.0.1541031464825', sep="^", header=None,
                      names=[name for name in col_name])
# print(demo_df.head())
# print(demo_df.info())
# print(demo_df.columns)
# print(demo_df.columns.values.tolist())


# 去掉 列全为NaN 的列 注意空值不等同于NaN,axis=1去掉列    all 指全为NaN时才去掉
# 可进一步去掉列为空的列
droped_demo_df = demo_df.dropna(axis=1, how='all')
# droped_demo_df

# 查看去掉NaN列后的 df 信息
# droped_demo_df.info()
# 查看去掉NaN列后 的列名及每列数据量
# droped_demo_df.count()

# 预先知道可以 groupby 成几组
# 根据列名EventClass 进行groupby  先查看可以分成几组及每组有多少数据
print(droped_demo_df.groupby(['EventClass']).size())
# print
# EventClass
# 100001        10
# 100002     14088
# 100011       103
# 100012       104
# 100016         1
# 100033    158477
# dtype: int64

# 根据列名EventClass groupby
groups = droped_demo_df.groupby(droped_demo_df['EventClass'])

for group in groups:
    # count 一下

    # print(type(group))             # <class 'tuple'>
    # print(group)
    group[1].to_csv('C:/Users/lx/Desktop/' + str(group[0]) + '.csv', index=False)  # , encoding='gbk')
print("success divided")
