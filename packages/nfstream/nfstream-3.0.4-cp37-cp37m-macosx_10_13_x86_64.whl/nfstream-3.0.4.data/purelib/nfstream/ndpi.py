"""
file: ndpi.py
This file is part of nfstream.

Copyright (C) 2019 - Zied Aouini <aouinizied@gmail.com>

nfstream is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

nfstream is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with nfstream.
If not, see <http://www.gnu.org/licenses/>.
"""

from os.path import abspath, dirname
import cffi
import sys

cc = """
typedef enum {
    ndpi_l4_proto_unknown = 0,
    ndpi_l4_proto_tcp_only,
    ndpi_l4_proto_udp_only,
    ndpi_l4_proto_tcp_and_udp,
} ndpi_l4_proto_info;
typedef enum {
    ndpi_no_tunnel = 0,
    ndpi_gtp_tunnel,
    ndpi_capwap_tunnel,
    ndpi_tzsp_tunnel,
    ndpi_l2tp_tunnel,
} ndpi_packet_tunnel;

typedef enum {
    ndpi_url_no_problem = 0,
    ndpi_url_possible_xss,
    ndpi_url_possible_sql_injection
} ndpi_url_risk;

/* NDPI_VISIT */
typedef enum {
    ndpi_preorder,
    ndpi_postorder,
    ndpi_endorder,
    ndpi_leaf
} ndpi_VISIT;

/* NDPI_NODE */
typedef struct node_t {
    char *key;
    struct node_t *left, *right;
} ndpi_node;

/* NDPI_MASK_SIZE */
typedef uint32_t ndpi_ndpi_mask;

/* NDPI_PROTO_BITMASK_STRUCT */
typedef struct ndpi_protocol_bitmask_struct {
    ndpi_ndpi_mask fds_bits[16];
} NDPI_PROTOCOL_BITMASK;

typedef struct spinlock {
    volatile int    val;
} spinlock_t;

typedef struct atomic {
    volatile int counter;
} atomic_t;

typedef long int time_t;

struct hash_ip4p_node {
    struct hash_ip4p_node   *next,*prev;
    time_t                  lchg;
    uint16_t               port,count:12,flag:4;
    uint32_t               ip;
    // + 12 bytes for ipv6
};

struct hash_ip4p {
    struct hash_ip4p_node   *top;
    spinlock_t              lock;
    size_t                  len;
};

struct hash_ip4p_table {
    size_t                  size;
    int			  ipv6;
    spinlock_t              lock;
    atomic_t                count;
    struct hash_ip4p        tbl;
};

struct bt_announce {              // 192 bytes
    uint32_t		hash[5];
    uint32_t		ip[4];
    uint32_t		time;
    uint16_t		port;
    uint8_t		name_len,
    name[149];     // 149 bytes
};

/* NDPI_PROTOCOL_TINC */
#define TINC_CACHE_MAX_SIZE 10

typedef enum {
    NDPI_HTTP_METHOD_UNKNOWN = 0,
    NDPI_HTTP_METHOD_OPTIONS,
    NDPI_HTTP_METHOD_GET,
    NDPI_HTTP_METHOD_HEAD,
    NDPI_HTTP_METHOD_PATCH,
    NDPI_HTTP_METHOD_POST,
    NDPI_HTTP_METHOD_PUT,
    NDPI_HTTP_METHOD_DELETE,
    NDPI_HTTP_METHOD_TRACE,
    NDPI_HTTP_METHOD_CONNECT
} ndpi_http_method;

struct ndpi_lru_cache_entry {
    uint32_t key; /* Store the whole key to avoid ambiguities */
    uint32_t is_full:1, value:16, pad:15;
};

struct ndpi_lru_cache {
    uint32_t num_entries;
    struct ndpi_lru_cache_entry *entries;
};

"""

cc_ndpi_network_headers = """
struct ndpi_chdlc
{
    uint8_t addr;          /* 0x0F (Unicast) - 0x8F (Broadcast) */
    uint8_t ctrl;          /* always 0x00                       */
    uint16_t proto_code;   /* protocol type (e.g. 0x0800 IP)    */
};

/* SLARP - Serial Line ARP http://tinyurl.com/qa54e95 */
struct ndpi_slarp
{
    /* address requests (0x00)
    address replies  (0x01)
    keep-alive       (0x02)
    */
    uint32_t slarp_type;
    uint32_t addr_1;
    uint32_t addr_2;
};

/* Cisco Discovery Protocol http://tinyurl.com/qa6yw9l */
struct ndpi_cdp
{
    uint8_t version;
    uint8_t ttl;
    uint16_t checksum;
    uint16_t type;
    uint16_t length;
};

/* +++++++++++++++ Ethernet header (IEEE 802.3) +++++++++++++++ */
struct ndpi_ethhdr
{
    uint8_t h_dest[6];       /* destination eth addr */
    uint8_t h_source[6];     /* source ether addr    */
    uint16_t h_proto;      /* data length (<= 1500) or type ID proto (>=1536) */
};

/* +++++++++++++++ ARP header +++++++++++++++ */
struct ndpi_arphdr 
{   
    uint16_t ar_hrd;/* Format of hardware address.  */
    uint16_t ar_pro;/* Format of protocol address.  */
    uint8_t  ar_hln;/* Length of hardware address.  */
    uint8_t  ar_pln;/* Length of protocol address.  */
    uint16_t ar_op;/* ARP opcode (command).  */
    uint8_t arp_sha[6];/* sender hardware address */
    uint32_t arp_spa;/* sender protocol address */
    uint8_t arp_tha[6];/* target hardware address */
    uint32_t arp_tpa;/* target protocol address */
};

/* +++++++++++++++ DHCP header +++++++++++++++ */
struct ndpi_dhcphdr {
    uint8_t      msgType;
    uint8_t      htype;
    uint8_t      hlen;
    uint8_t      hops;
    uint32_t     xid;/* 4 */
    uint16_t     secs;/* 8 */
    uint16_t     flags;
    uint32_t     ciaddr;/* 12 */
    uint32_t     yiaddr;/* 16 */
    uint32_t     siaddr;/* 20 */
    uint32_t     giaddr;/* 24 */
    uint8_t      chaddr[16]; /* 28 */
    uint8_t      sname[64]; /* 44 */
    uint8_t      file[128]; /* 108 */
    uint32_t     magic; /* 236 */
    uint8_t      options[308];
};

/* +++++++++++++++ MDNS rsp header +++++++++++++++ */
struct ndpi_mdns_rsp_entry {
    uint16_t rsp_type, rsp_class;
    uint32_t ttl;
    uint16_t data_len;
};

/* +++++++++++++++++++ LLC header (IEEE 802.2) ++++++++++++++++ */
struct ndpi_snap_extension
{
    uint16_t   oui;
    uint8_t    oui2;
    uint16_t   proto_ID;
};

struct ndpi_llc_header_snap
{
    uint8_t    dsap;
    uint8_t    ssap;
    uint8_t    ctrl;
    struct ndpi_snap_extension snap;
};

/* ++++++++++ RADIO TAP header (for IEEE 802.11) +++++++++++++ */
struct ndpi_radiotap_header
{
    uint8_t  version;         /* set to 0 */
    uint8_t  pad;
    uint16_t len;
    uint32_t present;
    uint64_t MAC_timestamp;
    uint8_t flags;
};

/* ++++++++++++ Wireless header (IEEE 802.11) ++++++++++++++++ */
struct ndpi_wifi_header
{
    uint16_t fc;
    uint16_t duration;
    uint8_t rcvr[6];
    uint8_t trsm[6];
    uint8_t dest[6];
    uint16_t seq_ctrl;
    /* uint64_t ccmp - for data encryption only - check fc.flag */
};

/* +++++++++++++++++++++++ MPLS header +++++++++++++++++++++++ */
struct ndpi_mpls_header
{
    uint32_t ttl:8, s:1, exp:3, label:20;
};

extern union mpls {
  uint32_t u32;
  struct ndpi_mpls_header mpls;
} mpls;

/* ++++++++++++++++++++++++ IP header ++++++++++++++++++++++++ */
struct ndpi_iphdr {
    uint8_t ihl:4, version:4;
    uint8_t tos;
    uint16_t tot_len;
    uint16_t id;
    uint16_t frag_off;
    uint8_t ttl;
    uint8_t protocol;
    uint16_t check;
    uint32_t saddr;
    uint32_t daddr;
};

/* +++++++++++++++++++++++ IPv6 header +++++++++++++++++++++++ */
/* rfc3542 */
struct ndpi_in6_addr {
    union {
        uint8_t   u6_addr8[16];
        uint16_t  u6_addr16[8];
        uint32_t  u6_addr32[4];
        uint64_t  u6_addr64[2];
    } u6_addr;  /* 128-bit IP6 address */
};

struct ndpi_ip6_hdrctl {
    uint32_t ip6_un1_flow;
    uint16_t ip6_un1_plen;
    uint8_t ip6_un1_nxt;
    uint8_t ip6_un1_hlim;
};

struct ndpi_ipv6hdr {
    struct ndpi_ip6_hdrctl ip6_hdr;
    struct ndpi_in6_addr ip6_src;
    struct ndpi_in6_addr ip6_dst;
};

/* +++++++++++++++++++++++ TCP header +++++++++++++++++++++++ */
struct ndpi_tcphdr
{
    uint16_t source;
    uint16_t dest;
    uint32_t seq;
    uint32_t ack_seq;
    uint16_t res1:4, doff:4, fin:1, syn:1, rst:1, psh:1, ack:1, urg:1, ece:1, cwr:1;
    uint16_t window;
    uint16_t check;
    uint16_t urg_ptr;
};

/* +++++++++++++++++++++++ UDP header +++++++++++++++++++++++ */
struct ndpi_udphdr
{
    uint16_t source;
    uint16_t dest;
    uint16_t len;
    uint16_t check;
};

struct ndpi_dns_packet_header {
    uint16_t tr_id;
    uint16_t flags;
    uint16_t num_queries;
    uint16_t num_answers;
    uint16_t authority_rrs;
    uint16_t additional_rrs;
};

typedef union
{
    uint32_t ipv4;
    uint8_t ipv4_uint8_t[4];
    struct ndpi_in6_addr ipv6;
} ndpi_ip_addr_t;


/* +++++++++++++++++++++++ ICMP header +++++++++++++++++++++++ */
struct ndpi_icmphdr {
    uint8_t type;/* message type */
    uint8_t code;/* type sub-code */
    uint16_t checksum;
    union {
        struct {
            uint16_t id;
            uint16_t sequence;
        } echo; /* echo datagram */

        uint32_t gateway; /* gateway address */
        struct {
            uint16_t _unused;
            uint16_t mtu;
        } frag;/* path mtu discovery */
    } un;
};

/* +++++++++++++++++++++++ ICMP6 header +++++++++++++++++++++++ */
struct ndpi_icmp6hdr {
  uint8_t     icmp6_type;   /* type field */
  uint8_t     icmp6_code;   /* code field */
  uint16_t    icmp6_cksum;  /* checksum field */
  union {
    uint32_t  icmp6_un_data32[1]; /* type-specific field */
    uint16_t  icmp6_un_data16[2]; /* type-specific field */
    uint8_t   icmp6_un_data8[4];  /* type-specific field */
  } icmp6_dataun;
};

/* +++++++++++++++++++++++ VXLAN header +++++++++++++++++++++++ */
struct ndpi_vxlanhdr {
    uint16_t flags;
    uint16_t groupPolicy;
    uint32_t vni;
};

struct tinc_cache_entry {
    uint32_t src_address;
    uint32_t dst_address;
    uint16_t dst_port;
};
"""

cc_ndpi_id_struct = """
struct ndpi_id_struct {
    /** detected_protocol_bitmask:
        access this bitmask to find out whether an id has used skype or not
        if a flag is set here, it will not be reset
        to compare this, use:
    **/
    NDPI_PROTOCOL_BITMASK detected_protocol_bitmask;
    /* NDPI_PROTOCOL_RTSP */
    ndpi_ip_addr_t rtsp_ip_address;
    /* NDPI_PROTOCOL_YAHOO */
    uint32_t yahoo_video_lan_timer;
    /* NDPI_PROTOCOL_IRC_MAXPORT % 2 must be 0 */
    /* NDPI_PROTOCOL_IRC */
    #define NDPI_PROTOCOL_IRC_MAXPORT 8
    uint16_t irc_port[NDPI_PROTOCOL_IRC_MAXPORT];
    uint32_t last_time_port_used[NDPI_PROTOCOL_IRC_MAXPORT];
    uint32_t irc_ts;
    /* NDPI_PROTOCOL_GNUTELLA */
    uint32_t gnutella_ts;
    /* NDPI_PROTOCOL_BATTLEFIELD */
    uint32_t battlefield_ts;
    /* NDPI_PROTOCOL_THUNDER */
    uint32_t thunder_ts;
    /* NDPI_PROTOCOL_RTSP */
    uint32_t rtsp_timer;
    /* NDPI_PROTOCOL_OSCAR */
    uint32_t oscar_last_safe_access_time;
    /* NDPI_PROTOCOL_ZATTOO */
    uint32_t zattoo_ts;
    /* NDPI_PROTOCOL_UNENCRYPTED_JABBER */
    uint32_t jabber_stun_or_ft_ts;
    /* NDPI_PROTOCOL_DIRECTCONNECT */
    uint32_t directconnect_last_safe_access_time;
    /* NDPI_PROTOCOL_SOULSEEK */
    uint32_t soulseek_last_safe_access_time;
    /* NDPI_PROTOCOL_DIRECTCONNECT */
    uint16_t detected_directconnect_port;
    uint16_t detected_directconnect_udp_port;
    uint16_t detected_directconnect_ssl_port;
    /* NDPI_PROTOCOL_BITTORRENT */
    #define NDPI_BT_PORTS 8
    uint16_t bt_port_t[NDPI_BT_PORTS];
    uint16_t bt_port_u[NDPI_BT_PORTS];
    /* NDPI_PROTOCOL_UNENCRYPTED_JABBER */
    #define JABBER_MAX_STUN_PORTS 6
    uint16_t jabber_voice_stun_port[JABBER_MAX_STUN_PORTS];
    uint16_t jabber_file_transfer_port[2];
    /* NDPI_PROTOCOL_GNUTELLA */
    uint16_t detected_gnutella_port;
    /* NDPI_PROTOCOL_GNUTELLA */
    uint16_t detected_gnutella_udp_port1;
    uint16_t detected_gnutella_udp_port2;
    /* NDPI_PROTOCOL_SOULSEEK */
    uint16_t soulseek_listen_port;
    /* NDPI_PROTOCOL_IRC */
    uint8_t irc_number_of_port;
    /* NDPI_PROTOCOL_OSCAR */
    uint8_t oscar_ssl_session_id[33];  
    /* NDPI_PROTOCOL_UNENCRYPTED_JABBER */
    uint8_t jabber_voice_stun_used_ports;
    /* NDPI_PROTOCOL_SIP */
    /* NDPI_PROTOCOL_YAHOO */
    uint32_t yahoo_video_lan_dir:1;
    /* NDPI_PROTOCOL_YAHOO */
    uint32_t yahoo_conf_logged_in:1;
    uint32_t yahoo_voice_conf_logged_in:1;
    /* NDPI_PROTOCOL_RTSP */
    uint32_t rtsp_ts_set:1;
};
"""
cc_ndpi_flow_tcp_struct = """
struct ndpi_flow_tcp_struct {
    /* NDPI_PROTOCOL_MAIL_SMTP */
    uint16_t smtp_command_bitmask;
    /* NDPI_PROTOCOL_MAIL_POP */
    uint16_t pop_command_bitmask;
    /* NDPI_PROTOCOL_QQ */
    uint16_t qq_nxt_len;
    /* NDPI_PROTOCOL_WHATSAPP */
    uint8_t wa_matched_so_far;
    /* NDPI_PROTOCOL_TDS */
    uint8_t tds_login_version;

    /* NDPI_PROTOCOL_IRC */
    uint8_t irc_stage;
    uint8_t irc_port;

    /* NDPI_PROTOCOL_H323 */
    uint8_t h323_valid_packets;

    /* NDPI_PROTOCOL_GNUTELLA */
    uint8_t gnutella_msg_id[3];

    /* NDPI_PROTOCOL_IRC */
    uint32_t irc_3a_counter:3;
    uint32_t irc_stage2:5;
    uint32_t irc_direction:2;
    uint32_t irc_0x1000_full:1;

    /* NDPI_PROTOCOL_SOULSEEK */
    uint32_t soulseek_stage:2;

    /* NDPI_PROTOCOL_TDS */
    uint32_t tds_stage:3;

    /* NDPI_PROTOCOL_USENET */
    uint32_t usenet_stage:2;

    /* NDPI_PROTOCOL_IMESH */
    uint32_t imesh_stage:4;

    /* NDPI_PROTOCOL_HTTP */
    uint32_t http_setup_dir:2;
    uint32_t http_stage:2;
    uint32_t http_empty_line_seen:1;
    uint32_t http_wait_for_retransmission:1;

    /* NDPI_PROTOCOL_GNUTELLA */
    uint32_t gnutella_stage:2;		       // 0 - 2
    /* NDPI_CONTENT_MMS */
    uint32_t mms_stage:2;
    /* NDPI_PROTOCOL_YAHOO */
    uint32_t yahoo_sip_comm:1;
    uint32_t yahoo_http_proxy_stage:2;

    /* NDPI_PROTOCOL_MSN */
    uint32_t msn_stage:3;
    uint32_t msn_ssl_ft:2;

    /* NDPI_PROTOCOL_SSH */
    uint32_t ssh_stage:3;

    /* NDPI_PROTOCOL_VNC */
    uint32_t vnc_stage:2;			// 0 - 3

    /* NDPI_PROTOCOL_TELNET */
    uint32_t telnet_stage:2;			// 0 - 2
    void* tls_srv_cert_fingerprint_ctx;

    /* NDPI_PROTOCOL_TLS */
    uint8_t tls_seen_client_cert:1,
    tls_seen_server_cert:1,
    tls_seen_certificate:1,
    tls_srv_cert_fingerprint_found:1,
    tls_srv_cert_fingerprint_processed:1,
    tls_stage:2, _pad:1; // 0 - 5
    int16_t tls_record_offset, tls_fingerprint_len; /* Need to be signed */
    uint8_t tls_sha1_certificate_fingerprint[20];

    /* NDPI_PROTOCOL_POSTGRES */
    uint32_t postgres_stage:3;

    /* NDPI_PROTOCOL_DIRECT_DOWNLOAD_LINK */
    uint32_t ddlink_server_direction:1;
    uint32_t seen_syn:1;
    uint32_t seen_syn_ack:1;
    uint32_t seen_ack:1;

    /* NDPI_PROTOCOL_ICECAST */
    uint32_t icecast_stage:1;

    /* NDPI_PROTOCOL_DOFUS */
    uint32_t dofus_stage:1;

    /* NDPI_PROTOCOL_FIESTA */
    uint32_t fiesta_stage:2;

    /* NDPI_PROTOCOL_WORLDOFWARCRAFT */
    uint32_t wow_stage:2;

    /* NDPI_PROTOCOL_HTTP_APPLICATION_VEOHTV */
    uint32_t veoh_tv_stage:2;

    /* NDPI_PROTOCOL_SHOUTCAST */
    uint32_t shoutcast_stage:2;

    /* NDPI_PROTOCOL_RTP */
    uint32_t rtp_special_packets_seen:1;

    /* NDPI_PROTOCOL_MAIL_POP */
    uint32_t mail_pop_stage:2;

    /* NDPI_PROTOCOL_MAIL_IMAP */
    uint32_t mail_imap_stage:3, mail_imap_starttls:2;

    /* NDPI_PROTOCOL_SKYPE */
    uint8_t skype_packet_id;

    /* NDPI_PROTOCOL_CITRIX */
    uint8_t citrix_packet_id;
    /* NDPI_PROTOCOL_LOTUS_NOTES */
    uint8_t lotus_notes_packet_id;

    /* NDPI_PROTOCOL_TEAMVIEWER */
    uint8_t teamviewer_stage;

    /* NDPI_PROTOCOL_ZMQ */
    uint8_t prev_zmq_pkt_len;
    uint8_t prev_zmq_pkt[10];

    /* NDPI_PROTOCOL_PPSTREAM */
    uint32_t ppstream_stage:3;

    /* NDPI_PROTOCOL_MEMCACHED */
    uint8_t memcached_matches;

    /* NDPI_PROTOCOL_NEST_LOG_SINK */
    uint8_t nest_log_sink_matches;
};
"""

cc_ndpi_flow_udp_struct = """
struct ndpi_flow_udp_struct {
    /* NDPI_PROTOCOL_BATTLEFIELD */
    uint32_t battlefield_msg_id;
    /* NDPI_PROTOCOL_SNMP */
    uint32_t snmp_msg_id;
    /* NDPI_PROTOCOL_BATTLEFIELD */
    uint32_t battlefield_stage:3;
    /* NDPI_PROTOCOL_SNMP */
    uint32_t snmp_stage:2;
    /* NDPI_PROTOCOL_PPSTREAM */
    uint32_t ppstream_stage:3;		  // 0 - 7
    /* NDPI_PROTOCOL_HALFLIFE2 */
    uint32_t halflife2_stage:2;		  // 0 - 2
    /* NDPI_PROTOCOL_TFTP */
    uint32_t tftp_stage:1;
    /* NDPI_PROTOCOL_AIMINI */
    uint32_t aimini_stage:5;
    /* NDPI_PROTOCOL_XBOX */
    uint32_t xbox_stage:1;
    /* NDPI_PROTOCOL_WINDOWS_UPDATE */
    uint32_t wsus_stage:1;
    /* NDPI_PROTOCOL_SKYPE */
    uint8_t skype_packet_id;
    /* NDPI_PROTOCOL_TEAMVIEWER */
    uint8_t teamviewer_stage;
    /* NDPI_PROTOCOL_EAQ */
    uint8_t eaq_pkt_id;
    uint32_t eaq_sequence;
    /* NDPI_PROTOCOL_RX */
    uint32_t rx_conn_epoch;
    uint32_t rx_conn_id;
    /* NDPI_PROTOCOL_MEMCACHED */
    uint8_t memcached_matches;
    /* NDPI_PROTOCOL_WIREGUARD */
    uint8_t wireguard_stage;
    uint32_t wireguard_peer_index[2];
};
"""

cc_ndpi_int_one_line_struct = """
struct ndpi_int_one_line_struct {
    const uint8_t *ptr;
    uint16_t len;
};
"""

cc_ndpi_packet_struct_stack = """
struct ndpi_packet_struct_stack {
    uint8_t detected_subprotocol_stack[2];
    uint16_t protocol_stack_info;
};
struct ndpi_flow_struct_stack {
    uint16_t detected_protocol_stack[2];
    uint16_t protocol_stack_info;
};
"""

cc_ndpi_packet_struct = """
struct ndpi_packet_struct {
    const struct ndpi_iphdr *iph;
    const struct ndpi_ipv6hdr *iphv6;
    const struct ndpi_tcphdr *tcp;
    const struct ndpi_udphdr *udp;
    const uint8_t *generic_l4_ptr;	/* is set only for non tcp-udp traffic */
    const uint8_t *payload;
    uint32_t tick_timestamp;
    uint64_t tick_timestamp_l;
    struct ndpi_packet_struct_stack ndpi_packet_stack;
    struct ndpi_int_one_line_struct line[64];
    /* HTTP headers */
    struct ndpi_int_one_line_struct host_line;
    struct ndpi_int_one_line_struct forwarded_line;
    struct ndpi_int_one_line_struct referer_line;
    struct ndpi_int_one_line_struct content_line;
    struct ndpi_int_one_line_struct accept_line;
    struct ndpi_int_one_line_struct user_agent_line;
    struct ndpi_int_one_line_struct http_url_name;
    struct ndpi_int_one_line_struct http_encoding;
    struct ndpi_int_one_line_struct http_transfer_encoding;
    struct ndpi_int_one_line_struct http_contentlen;
    struct ndpi_int_one_line_struct http_cookie;
    struct ndpi_int_one_line_struct http_origin;
    struct ndpi_int_one_line_struct http_x_session_type;
    struct ndpi_int_one_line_struct server_line;
    struct ndpi_int_one_line_struct http_method;
    struct ndpi_int_one_line_struct http_response; /* the first "word" in this pointer is the response code in the 
                                                      packet (200, etc) */
    uint8_t http_num_headers; /* number of found (valid) header lines in HTTP request or response */
    uint16_t l3_packet_len;
    uint16_t l4_packet_len;
    uint16_t payload_packet_len;
    uint16_t actual_payload_len;
    uint16_t num_retried_bytes;
    uint16_t parsed_lines;
    uint16_t parsed_unix_lines;
    uint16_t empty_line_position;
    uint8_t tcp_retransmission;
    uint8_t l4_protocol;
    uint8_t tls_certificate_detected:4, tls_certificate_num_checks:4;
    uint8_t packet_lines_parsed_complete:1,
    packet_direction:1, empty_line_position_set:1, pad:5;
};
struct ndpi_detection_module_struct;
struct ndpi_flow_struct;
struct ndpi_call_function_struct {
    NDPI_PROTOCOL_BITMASK detection_bitmask;
    NDPI_PROTOCOL_BITMASK excluded_protocol_bitmask;
    uint32_t ndpi_selection_bitmask;
    void (*func) (struct ndpi_detection_module_struct *, struct ndpi_flow_struct *flow);
    uint8_t detection_feature;
};
struct ndpi_subprotocol_conf_struct {
    void (*func) (struct ndpi_detection_module_struct *, char *attr, char *value, int protocol_id);
};

typedef struct {
    uint16_t port_low, port_high;
} ndpi_port_range;

typedef enum {
    NDPI_PROTOCOL_SAFE = 0,              /* Surely doesn't provide risks for the network. (e.g., a news site) */
    NDPI_PROTOCOL_ACCEPTABLE,            /* Probably doesn't provide risks, but could be malicious (e.g., Dropbox) */
    NDPI_PROTOCOL_FUN,                   /* Pure fun protocol, which may be prohibited by the user policy (e.g., Netflix) */
    NDPI_PROTOCOL_UNSAFE,                /* Probably provides risks, but could be a normal traffic. Unencrypted protocols with clear pass should be here (e.g., telnet) */
    NDPI_PROTOCOL_POTENTIALLY_DANGEROUS, /* Possibly dangerous (ex. Tor). */
    NDPI_PROTOCOL_DANGEROUS,             /* Surely is dangerous (ex. smbv1). Be prepared to troubles */
    NDPI_PROTOCOL_TRACKER_ADS,           /* Trackers, Advertisements... */
    NDPI_PROTOCOL_UNRATED                /* No idea, not implemented or impossible to classify */
} ndpi_protocol_breed_t;

#define NUM_BREEDS 8

/* Abstract categories to group the protocols. */
typedef enum {
    NDPI_PROTOCOL_CATEGORY_UNSPECIFIED = 0,   /* For general services and unknown protocols */
    NDPI_PROTOCOL_CATEGORY_MEDIA,             /* Multimedia and streaming */
    NDPI_PROTOCOL_CATEGORY_VPN,               /* Virtual Private Networks */
    NDPI_PROTOCOL_CATEGORY_MAIL,              /* Protocols to send/receive/sync emails */
    NDPI_PROTOCOL_CATEGORY_DATA_TRANSFER,     /* AFS/NFS and similar protocols */
    NDPI_PROTOCOL_CATEGORY_WEB,               /* Web/mobile protocols and services */
    NDPI_PROTOCOL_CATEGORY_SOCIAL_NETWORK,    /* Social networks */
    NDPI_PROTOCOL_CATEGORY_DOWNLOAD_FT,       /* Download, FTP, file transfer/sharing */
    NDPI_PROTOCOL_CATEGORY_GAME,              /* Online games */
    NDPI_PROTOCOL_CATEGORY_CHAT,              /* Instant messaging */
    NDPI_PROTOCOL_CATEGORY_VOIP,              /* Real-time communications and conferencing */
    NDPI_PROTOCOL_CATEGORY_DATABASE,          /* Protocols for database communication */
    NDPI_PROTOCOL_CATEGORY_REMOTE_ACCESS,     /* Remote access and control */
    NDPI_PROTOCOL_CATEGORY_CLOUD,             /* Online cloud services */
    NDPI_PROTOCOL_CATEGORY_NETWORK,           /* Network infrastructure protocols */
    NDPI_PROTOCOL_CATEGORY_COLLABORATIVE,     /* Software for collaborative development, including Webmail */
    NDPI_PROTOCOL_CATEGORY_RPC,               /* High level network communication protocols */
    NDPI_PROTOCOL_CATEGORY_STREAMING,         /* Streaming protocols */
    NDPI_PROTOCOL_CATEGORY_SYSTEM_OS,         /* System/Operating System level applications */
    NDPI_PROTOCOL_CATEGORY_SW_UPDATE,         /* Software update */

    /* See #define NUM_CUSTOM_CATEGORIES */
    NDPI_PROTOCOL_CATEGORY_CUSTOM_1,          /* User custom category 1 */
    NDPI_PROTOCOL_CATEGORY_CUSTOM_2,          /* User custom category 2 */
    NDPI_PROTOCOL_CATEGORY_CUSTOM_3,          /* User custom category 3 */
    NDPI_PROTOCOL_CATEGORY_CUSTOM_4,          /* User custom category 4 */
    NDPI_PROTOCOL_CATEGORY_CUSTOM_5,          /* User custom category 5 */

    /* Further categories... */
    NDPI_PROTOCOL_CATEGORY_MUSIC,
    NDPI_PROTOCOL_CATEGORY_VIDEO,
    NDPI_PROTOCOL_CATEGORY_SHOPPING,
    NDPI_PROTOCOL_CATEGORY_PRODUCTIVITY,
    NDPI_PROTOCOL_CATEGORY_FILE_SHARING,

    /* Some custom categories */
    CUSTOM_CATEGORY_MINING           = 99,
    CUSTOM_CATEGORY_MALWARE          = 100,
    CUSTOM_CATEGORY_ADVERTISEMENT    = 101,
    CUSTOM_CATEGORY_BANNED_SITE      = 102,
    CUSTOM_CATEGORY_SITE_UNAVAILABLE = 103,
    CUSTOM_CATEGORY_ALLOWED_SITE     = 104,
    /*
        The category below is used to track communications made by
        security applications (e.g. sophosxl.net, spamhaus.org)
        to track malware, spam etc.
    */
    CUSTOM_CATEGORY_ANTIMALWARE      = 105,
    /*
        IMPORTANT
        Please keep in sync with
        static const char* categories[] = { ..}
        in ndpi_main.c
    */
    NDPI_PROTOCOL_NUM_CATEGORIES
    /*
        NOTE: Keep this as last member
        Unused as value but useful to getting the number of elements
        in this datastructure
    */
} ndpi_protocol_category_t;

typedef enum {
    ndpi_pref_direction_detect_disable = 0,
    ndpi_pref_disable_metadata_export,
} ndpi_detection_preference;

/* ntop extensions */
typedef struct ndpi_proto_defaults {
    char *protoName;
    ndpi_protocol_category_t protoCategory;
    uint8_t can_have_a_subprotocol;
    uint16_t protoId, protoIdx;
    uint16_t master_tcp_protoId[2], master_udp_protoId[2]; /* The main protocols on which this sub-protocol sits on */
    ndpi_protocol_breed_t protoBreed;
    void (*func) (struct ndpi_detection_module_struct *, struct ndpi_flow_struct *flow);
} ndpi_proto_defaults_t;

typedef struct ndpi_default_ports_tree_node {
    ndpi_proto_defaults_t *proto;
    uint8_t customUserProto;
    uint16_t default_port;
} ndpi_default_ports_tree_node_t;

typedef struct _ndpi_automa {
    void *ac_automa; /* Real type is AC_AUTOMATA_t */
    uint8_t ac_automa_finalized;
} ndpi_automa;

typedef struct ndpi_proto {
    /*
        Note
        below we do not use ndpi_protocol_id_t as users can define their own
        custom protocols and thus the typedef could be too short in size.
    */
    uint16_t master_protocol /* e.g. HTTP */, app_protocol /* e.g. FaceBook */;
    ndpi_protocol_category_t category;
} ndpi_protocol;

#define NUM_CUSTOM_CATEGORIES      5
#define CUSTOM_CATEGORY_LABEL_LEN 32

typedef enum {
    NDPI_LOG_ERROR,
    NDPI_LOG_TRACE,
    NDPI_LOG_DEBUG,
    NDPI_LOG_DEBUG_EXTRA
} ndpi_log_level_t;


struct ndpi_detection_module_struct {
    NDPI_PROTOCOL_BITMASK detection_bitmask;
    NDPI_PROTOCOL_BITMASK generic_http_packet_bitmask;
    uint32_t current_ts;
    uint32_t ticks_per_second;
    char custom_category_labels[NUM_CUSTOM_CATEGORIES][CUSTOM_CATEGORY_LABEL_LEN];
    /* callback function buffer */
    struct ndpi_call_function_struct callback_buffer[250];
    uint32_t callback_buffer_size;
    struct ndpi_call_function_struct callback_buffer_tcp_no_payload[250];
    uint32_t callback_buffer_size_tcp_no_payload;
    struct ndpi_call_function_struct callback_buffer_tcp_payload[250];
    uint32_t callback_buffer_size_tcp_payload;
    struct ndpi_call_function_struct callback_buffer_udp[250];
    uint32_t callback_buffer_size_udp;
    struct ndpi_call_function_struct callback_buffer_non_tcp_udp[250];
    uint32_t callback_buffer_size_non_tcp_udp;
    ndpi_default_ports_tree_node_t *tcpRoot, *udpRoot;
    ndpi_log_level_t ndpi_log_level; /* default error */
    /* misc parameters */
    uint32_t tcp_max_retransmission_window_size;
    uint32_t directconnect_connection_ip_tick_timeout;
    /* subprotocol registration handler */
    struct ndpi_subprotocol_conf_struct subprotocol_conf[250];
    unsigned ndpi_num_supported_protocols;
    unsigned ndpi_num_custom_protocols;
    /* HTTP/DNS/HTTPS host matching */
    ndpi_automa host_automa,                     /* Used for DNS/HTTPS */
    content_automa,                            /* Used for HTTP subprotocol_detection */
    subprotocol_automa,                        /* Used for HTTP subprotocol_detection */
    bigrams_automa, impossible_bigrams_automa; /* TOR */
    /* IMPORTANT: please update ndpi_finalize_initalization() whenever you add a new automa */

    struct {
        ndpi_automa hostnames, hostnames_shadow;
        void *ipAddresses, *ipAddresses_shadow; /* Patricia */
        uint8_t categories_loaded;
    } custom_categories;

    /* IP-based protocol detection */
    void *protocols_ptree;

    /* irc parameters */
    uint32_t irc_timeout;
    /* gnutella parameters */
    uint32_t gnutella_timeout;
    /* battlefield parameters */
    uint32_t battlefield_timeout;
    /* thunder parameters */
    uint32_t thunder_timeout;
    /* SoulSeek parameters */
    uint32_t soulseek_connection_ip_tick_timeout;
    /* rtsp parameters */
    uint32_t rtsp_connection_timeout;
    /* tvants parameters */
    uint32_t tvants_connection_timeout;
    /* rstp */
    uint32_t orb_rstp_ts_timeout;
    /* yahoo */
    uint8_t yahoo_detect_http_connections;
    uint32_t yahoo_lan_video_timeout;
    uint32_t zattoo_connection_timeout;
    uint32_t jabber_stun_timeout;
    uint32_t jabber_file_transfer_timeout;
    uint8_t ip_version_limit;
    /* NDPI_PROTOCOL_BITTORRENT */
    struct hash_ip4p_table *bt_ht;
    struct hash_ip4p_table *bt6_ht;

    /* BT_ANNOUNCE */
    struct bt_announce *bt_ann;
    int    bt_ann_len;

    /* NDPI_PROTOCOL_OOKLA */
    struct ndpi_lru_cache *ookla_cache;
    /* NDPI_PROTOCOL_TINC */
    struct cache *tinc_cache;
    /* NDPI_PROTOCOL_STUN and subprotocols */
    struct ndpi_lru_cache *stun_cache;
    ndpi_proto_defaults_t proto_defaults[512];
    uint8_t direction_detect_disable:1, /* disable internal detection of packet direction */
    disable_metadata_export:1   /* No metadata is exported */
    ;
    void *hyperscan; /* Intel Hyperscan */
};

#define NDPI_CIPHER_SAFE                        0
#define NDPI_CIPHER_WEAK                        1
#define NDPI_CIPHER_INSECURE                    2

typedef enum {
    ndpi_cipher_safe = NDPI_CIPHER_SAFE,
    ndpi_cipher_weak = NDPI_CIPHER_WEAK,
    ndpi_cipher_insecure = NDPI_CIPHER_INSECURE
} ndpi_cipher_weakness;

struct ndpi_flow_struct {
  struct ndpi_flow_struct_stack ndpi_flow_stack;
  /* init parameter, internal used to set up timestamp,... */
  uint16_t guessed_protocol_id, guessed_host_protocol_id, guessed_category, guessed_header_category;
  uint8_t l4_proto, protocol_id_already_guessed:1, host_already_guessed:1, init_finished:1, setup_packet_direction:1, packet_direction:1, check_extra_packets:1;

  /*
    if ndpi_struct->direction_detect_disable == 1
    tcp sequence number connection tracking
  */
  uint32_t next_tcp_seq_nr[2];

  uint8_t max_extra_packets_to_check;
  uint8_t num_extra_packets_checked;
  uint8_t num_processed_pkts; /* <= WARNING it can wrap but we do expect people to giveup earlier */

  int (*extra_packets_func) (struct ndpi_detection_module_struct *, struct ndpi_flow_struct *flow);

  /*
    the tcp / udp / other l4 value union
    used to reduce the number of bytes for tcp or udp protocol states
  */
  union {
    struct ndpi_flow_tcp_struct tcp;
    struct ndpi_flow_udp_struct udp;
  } l4;

  /*
    Pointer to src or dst that identifies the
    server of this connection
  */
  struct ndpi_id_struct *server_id;
  /* HTTP host or DNS query */
  uint8_t host_server_name[256];

  /*
    This structure below will not not stay inside the protos
    structure below as HTTP is used by many subprotocols
    such as FaceBook, Google... so it is hard to know
    when to use it or not. Thus we leave it outside for the
    time being.
  */
  struct {
    ndpi_http_method method;
    char *url, *content_type;
    uint8_t num_request_headers, num_response_headers;
    uint8_t request_version; /* 0=1.0 and 1=1.1. Create an enum for this? */
    uint16_t response_status_code; /* 200, 404, etc. */
  } http;

  union {
    /* the only fields useful for nDPI and ntopng */
    struct {
      uint8_t num_queries, num_answers, reply_code, is_query;
      uint16_t query_type, query_class, rsp_type;
      ndpi_ip_addr_t rsp_addr; /* The first address in a DNS response packet */
    } dns;

    struct {
      uint8_t request_code;
      uint8_t version;
    } ntp;

    struct {
      char cname[24], realm[24];
    } kerberos;

    struct {
      struct {
	uint16_t ssl_version;
	char client_certificate[64], server_certificate[64], server_organization[64];
	uint32_t notBefore, notAfter;
	char ja3_client[33], ja3_server[33];
	uint16_t server_cipher;
	ndpi_cipher_weakness server_unsafe_cipher;
      } ssl;

      struct {
	uint8_t num_udp_pkts, num_processed_pkts, num_binding_requests;
      } stun;

      /* We can have STUN over SSL/TLS thus they need to live together */
    } stun_ssl;

    struct {
      char client_signature[48], server_signature[48];
      char hassh_client[33], hassh_server[33];
    } ssh;

    struct {
      uint8_t last_one_byte_pkt, last_byte;
    } imo;

    struct {
      char answer[96];
    } mdns;

    struct {
      char version[32];
    } ubntac2;

    struct {
      /* Via HTTP User-Agent */
      uint8_t detected_os[32];
      /* Via HTTP X-Forwarded-For */
      uint8_t nat_ip[24];
    } http;

    struct {
      /* Bittorrent hash */
      uint8_t hash[20];
    } bittorrent;

    struct {
      char fingerprint[48];
      char class_ident[48];
    } dhcp;
  } protos;

  /*** ALL protocol specific 64 bit variables here ***/

  /* protocols which have marked a connection as this connection cannot be protocol XXX, multiple uint64_t */
  NDPI_PROTOCOL_BITMASK excluded_protocol_bitmask;

  ndpi_protocol_category_t category;

  /* NDPI_PROTOCOL_REDIS */
  uint8_t redis_s2d_first_char, redis_d2s_first_char;

  uint16_t packet_counter;		      // can be 0 - 65000
  uint16_t packet_direction_counter[2];
  uint16_t byte_counter[2];
  /* NDPI_PROTOCOL_BITTORRENT */
  uint8_t bittorrent_stage;		      // can be 0 - 255

  /* NDPI_PROTOCOL_DIRECTCONNECT */
  uint8_t directconnect_stage:2;	      // 0 - 1

  /* NDPI_PROTOCOL_YAHOO */
  uint8_t sip_yahoo_voice:1;

  /* NDPI_PROTOCOL_HTTP */
  uint8_t http_detected:1;
  uint16_t http_upper_protocol, http_lower_protocol;

  /* NDPI_PROTOCOL_RTSP */
  uint8_t rtsprdt_stage:2, rtsp_control_flow:1;

  /* NDPI_PROTOCOL_YAHOO */
  uint8_t yahoo_detection_finished:2;

  /* NDPI_PROTOCOL_ZATTOO */
  uint8_t zattoo_stage:3;

  /* NDPI_PROTOCOL_QQ */
  uint8_t qq_stage:3;

  /* NDPI_PROTOCOL_THUNDER */
  uint8_t thunder_stage:2;		        // 0 - 3

  /* NDPI_PROTOCOL_OSCAR */
  uint8_t oscar_ssl_voice_stage:3, oscar_video_voice:1;

  /* NDPI_PROTOCOL_FLORENSIA */
  uint8_t florensia_stage:1;

  /* NDPI_PROTOCOL_SOCKS */
  uint8_t socks5_stage:2, socks4_stage:2;      // 0 - 3

  /* NDPI_PROTOCOL_EDONKEY */
  uint8_t edonkey_stage:2;	                // 0 - 3

  /* NDPI_PROTOCOL_FTP_CONTROL */
  uint8_t ftp_control_stage:2;

  /* NDPI_PROTOCOL_RTMP */
  uint8_t rtmp_stage:2;

  /* NDPI_PROTOCOL_PANDO */
  uint8_t pando_stage:3;

  /* NDPI_PROTOCOL_STEAM */
  uint16_t steam_stage:3, steam_stage1:3, steam_stage2:2, steam_stage3:2;

  /* NDPI_PROTOCOL_PPLIVE */
  uint8_t pplive_stage1:3, pplive_stage2:2, pplive_stage3:2;

  /* NDPI_PROTOCOL_STARCRAFT */
  uint8_t starcraft_udp_stage : 3;	// 0-7

  /* NDPI_PROTOCOL_OPENVPN */
  uint8_t ovpn_session_id[8];
  uint8_t ovpn_counter;

  /* NDPI_PROTOCOL_TINC */
  uint8_t tinc_state;
  struct tinc_cache_entry tinc_cache_entry;

  /* NDPI_PROTOCOL_CSGO */
  uint8_t csgo_strid[18],csgo_state,csgo_s2;
  uint32_t csgo_id2;

  /* NDPI_PROTOCOL_1KXUN || NDPI_PROTOCOL_IQIYI */
  uint16_t kxun_counter, iqiyi_counter;

  /* internal structures to save functions calls */
  struct ndpi_packet_struct packet;
  struct ndpi_flow_struct *flow;
  struct ndpi_id_struct *src;
  struct ndpi_id_struct *dst;
};
typedef struct {
    char *string_to_match, *string2_to_match, *pattern_to_match, *proto_name;
    int protocol_id;
    ndpi_protocol_category_t protocol_category;
    ndpi_protocol_breed_t protocol_breed;
} ndpi_protocol_match;

typedef struct {
    char *string_to_match, *hyperscan_string_to_match;
    ndpi_protocol_category_t protocol_category;
} ndpi_category_match;

typedef struct {
    uint32_t network;
    uint8_t cidr;
    uint8_t value;
} ndpi_network;

typedef uint32_t ndpi_init_prefs;

typedef enum 
{
    ndpi_no_prefs = 0,
    ndpi_dont_load_tor_hosts,
} ndpi_prefs;

typedef struct {
    int protocol_id;
    ndpi_protocol_category_t protocol_category;
    ndpi_protocol_breed_t protocol_breed;
} ndpi_protocol_match_result;

#define DEFAULT_SERIES_LEN  64
#define MAX_SERIES_LEN      512
#define MIN_SERIES_LEN      8
"""

cc_ndpi_apis = """
struct ndpi_detection_module_struct *ndpi_init_detection_module(void);
void *memset(void *str, int c, size_t n);
void ndpi_set_protocol_detection_bitmask2(struct ndpi_detection_module_struct *ndpi_struct, 
                                          const NDPI_PROTOCOL_BITMASK * detection_bitmask);
ndpi_protocol ndpi_detection_process_packet(struct ndpi_detection_module_struct *ndpi_struct,
                                            struct ndpi_flow_struct *flow,
                                            const unsigned char *packet,
                                            const unsigned short packetlen,
                                            const uint64_t current_tick,
                                            struct ndpi_id_struct *src,
                                            struct ndpi_id_struct *dst);
ndpi_protocol ndpi_detection_giveup(struct ndpi_detection_module_struct *ndpi_struct,
                                    struct ndpi_flow_struct *flow,
                                    uint8_t enable_guess,
                                    uint8_t *protocol_was_guessed);

void * ndpi_malloc(size_t size);
void   ndpi_free(void *ptr);
void * ndpi_flow_malloc(size_t size);
void  ndpi_flow_free(void *ptr);
void ndpi_exit_detection_module(struct ndpi_detection_module_struct *ndpi_struct);
char* ndpi_protocol2name(struct ndpi_detection_module_struct *ndpi_mod, ndpi_protocol proto, char *buf, unsigned buf_len);
const char* ndpi_category_get_name(struct ndpi_detection_module_struct *ndpi_mod, ndpi_protocol_category_t category);
char* ndpi_revision(void);
void ndpi_finalize_initalization(struct ndpi_detection_module_struct *ndpi_str);
"""


class NDPI():
    def __init__(self, libpath=None, max_tcp_dissections=10, max_udp_dissections=16):
        self._ffi = cffi.FFI()
        if libpath is None:
            if "win" in sys.platform[:3]:
                self._ndpi = self._ffi.dlopen(dirname(abspath(__file__)) + '/libs/libndpi.a')
            else:
                self._ndpi = self._ffi.dlopen(dirname(abspath(__file__)) + '/libs/libndpi.so')
        else:
            self._ndpi = self._ffi.dlopen(libpath)
        self._ffi.cdef(cc)
        self._ffi.cdef(cc_ndpi_network_headers, packed=True)
        self._ffi.cdef(cc_ndpi_id_struct)
        self._ffi.cdef(cc_ndpi_flow_tcp_struct, packed=True)
        self._ffi.cdef(cc_ndpi_flow_udp_struct, packed=True)
        self._ffi.cdef(cc_ndpi_int_one_line_struct)
        self._ffi.cdef(cc_ndpi_packet_struct_stack, packed=True)
        self._ffi.cdef(cc_ndpi_packet_struct)
        self._ffi.cdef(cc_ndpi_apis)
        self._mod = self._ndpi.ndpi_init_detection_module()
        ndpi_revision = self._ffi.string(self._ndpi.ndpi_revision()).decode('utf-8', errors='ignore')
        if ndpi_revision[:3] >= '3.1':
            self._ndpi.ndpi_finalize_initalization(self._mod)
        all = self._ffi.new('NDPI_PROTOCOL_BITMASK*')
        self._ndpi.memset(self._ffi.cast("char *", all), 0xFF, self._ffi.sizeof("NDPI_PROTOCOL_BITMASK"))
        self._ndpi.ndpi_set_protocol_detection_bitmask2(self._mod, all)
        self.SIZEOF_FLOW_STRUCT = self._ffi.sizeof("struct ndpi_flow_struct")
        self.SIZEOF_ID_STRUCT = self._ffi.sizeof("struct ndpi_id_struct")
        self.NULL = self._ffi.NULL
        self.max_tcp_dissections = max_tcp_dissections
        self.max_udp_dissections = max_udp_dissections

    def new_ndpi_flow(self):
        f = self._ffi.cast('struct ndpi_flow_struct*', self._ndpi.ndpi_flow_malloc(self.SIZEOF_FLOW_STRUCT))
        self._ndpi.memset(f, 0, self.SIZEOF_FLOW_STRUCT)
        return f

    def new_ndpi_id(self):
        i = self._ffi.cast('struct ndpi_id_struct*', self._ndpi.ndpi_malloc(self.SIZEOF_ID_STRUCT))
        self._ndpi.memset(i, 0, self.SIZEOF_ID_STRUCT)
        return i

    def ndpi_detection_process_packet(self, flow, packet, packetlen, current_tick, src, dst):
        return self._ndpi.ndpi_detection_process_packet(self._mod, flow, packet, packetlen, current_tick, src, dst)

    def ndpi_detection_giveup(self, flow):
        return self._ndpi.ndpi_detection_giveup(self._mod, flow, 1, self._ffi.new("uint8_t*", 0))

    def ndpi_flow_free(self, flow):
        return self._ndpi.ndpi_flow_free(flow)

    def ndpi_free(self, ptr):
        return self._ndpi.ndpi_free(ptr)

    def get_str_field(self, ptr):
        return self._ffi.string(ptr).decode('utf-8', errors='ignore')

    def ndpi_protocol2name(self, proto):
        buf = self._ffi.new("char[32]")
        self._ndpi.ndpi_protocol2name(self._mod, proto, buf, self._ffi.sizeof(buf))
        return self._ffi.string(buf).decode('utf-8', errors='ignore')

    def ndpi_category_get_name(self, category):
        return self._ffi.string(self._ndpi.ndpi_category_get_name(self._mod, category)).decode('utf-8', errors='ignore')

    def ndpi_exit_detection_module(self):
        self._ndpi.ndpi_exit_detection_module(self._mod)