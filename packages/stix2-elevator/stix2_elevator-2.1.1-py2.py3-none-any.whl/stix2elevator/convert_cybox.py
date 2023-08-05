import re

from cybox.objects.account_object import Account
from cybox.objects.address_object import Address
from cybox.objects.archive_file_object import ArchiveFile
from cybox.objects.artifact_object import Artifact
from cybox.objects.domain_name_object import DomainName
from cybox.objects.email_message_object import EmailMessage
from cybox.objects.file_object import File
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.mutex_object import Mutex
from cybox.objects.network_connection_object import NetworkConnection
from cybox.objects.network_packet_object import NetworkPacket
from cybox.objects.network_socket_object import NetworkSocket
from cybox.objects.port_object import Port
from cybox.objects.process_object import Process
from cybox.objects.unix_user_account_object import UnixUserAccount
from cybox.objects.uri_object import URI
from cybox.objects.user_account_object import UserAccount
from cybox.objects.win_computer_account_object import WinComputerAccount
from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.objects.win_process_object import WinProcess
from cybox.objects.win_registry_key_object import WinRegistryKey
from cybox.objects.win_service_object import WinService
import netaddr
from six import text_type

from stix2elevator.common import ADDRESS_FAMILY_ENUMERATION, SOCKET_OPTIONS
from stix2elevator.ids import (add_id_value,
                               add_object_id_value,
                               generate_sco_id,
                               get_id_value,
                               get_object_id_value)
from stix2elevator.missing_policy import (convert_to_custom_property_name,
                                          handle_missing_string_property)
from stix2elevator.options import error, get_option_value, info, warn
from stix2elevator.utils import (convert_timestamp_to_string,
                                 map_vocabs_to_label)
from stix2elevator.vocab_mappings import (SERVICE_START_TYPE,
                                          SERVICE_STATUS,
                                          SERVICE_TYPE,
                                          WINDOWS_PEBINARY)


def create_base_sco(obj1x, type, other_properties=None):
    if other_properties:
        new_dict = other_properties
        new_dict["type"] = type
    else:
        new_dict = {"type": type}
    return new_dict


def finish_sco(instance, stix1x_id):
    if get_option_value("spec_version") == "2.1":
        instance["id"] = generate_sco_id(instance["type"], instance)
        if stix1x_id:
            add_id_value(stix1x_id, instance["id"])


def convert_account(acc, obj1x_id):
    account_dict = create_base_sco(acc, "user-account")
    if acc.creation_date:
        account_dict["account_created"] = acc.creation_date.value
    if acc.last_accessed_time:
        account_dict["account_last_login"] = acc.last_accessed_time
    if acc.disabled:
        account_dict["is_disabled"] = acc.disabled
    if acc.authentication and get_option_value("spec_version") == "2.1":
        if acc.authentication.authentication_data:
            account_dict["credential"] = acc.authentication.authentication_data
    if isinstance(acc, UserAccount):
        if acc.username:
            account_dict["account_login"] = acc.username.value
        if acc.full_name:
            account_dict["display_name"] = acc.full_name.value
        if acc.last_login:
            account_dict["account_last_login"] = convert_timestamp_to_string(acc.last_login.value)
        if isinstance(acc, UnixUserAccount):
            account_dict["account_type"] = "unix"
            ext_dict = {}
            if acc.group_id:
                ext_dict["gid"] = acc.group_id.value
            if acc.user_id:
                account_dict["user_id"] = text_type(acc.user_id.value)
            if acc.login_shell:
                ext_dict["shell"] = acc.login_shell.value
            if acc.home_directory:
                ext_dict["home_dir"] = acc.home_directory.value
            if acc.group_list:
                ext_dict["groups"] = []
                for g in acc.group_list:
                    ext_dict["groups"].append(text_type(g.group_id.value))
            if ext_dict != {}:
                account_dict["extensions"] = {"unix-account-ext": ext_dict}
        elif isinstance(acc, WinComputerAccount):
            if acc.domain:
                account_dict["account_type"] = "windows-domain"
            else:
                account_dict["account_type"] = "windows-local"
    finish_sco(account_dict, obj1x_id)
    return account_dict


def handle_inclusive_ip_addresses(add_value, obj1x_id):
    if add_value.condition == 'InclusiveBetween' and isinstance(add_value.value, list):
        x = str(netaddr.iprange_to_cidrs(add_value.value[0], add_value.value[1]))
        m = re.match(r".*'(\d+.\d+.\d+.\d+/\d+).*", x)
        if m:
            return m.group(1)
        else:
            warn("Cannot convert range of %s to %s in %s to a CIDR", 501, add_value.value[0], add_value.value[1], obj1x_id)
            return None
    else:
        return add_value.value


def convert_address(add, obj1x_id=None):
    if add.category == add.CAT_IPV4:
        instance = create_base_sco(add, "ipv4-addr", {"value": handle_inclusive_ip_addresses(add.address_value, obj1x_id)})
    elif add.category == add.CAT_IPV6:
        # TODO: handle ipv6 CIDRs
        instance = create_base_sco(add, "ipv6-addr", {"value": add.address_value.value})
    elif add.category == add.CAT_MAC:
        instance = create_base_sco(add, "mac-addr", {"value": add.address_value.value})
    elif add.category == add.CAT_EMAIL:
        instance = create_base_sco(add, "email-addr", {"value": add.address_value.value})
    else:
        warn("The address type %s is not part of STIX 2.x", 421, add.category)
        return None
    if instance:
        finish_sco(instance, obj1x_id)
        return instance


def convert_artifact_compression(c):
    compression_dict = dict()
    if c.compression_mechanism:
        compression_dict[convert_to_custom_property_name("compression_mechanism")] = c.compression_mechanism
    if c.compression_mechanism_ref:
        compression_dict[convert_to_custom_property_name("compression_mechanism_ref")] = c.compression_mechanism_ref
    return compression_dict


def convert_artifact_encoding(e):
    encoding_dict = dict()
    if e.algorithm:
        encoding_dict[convert_to_custom_property_name("algorithmm")] = e.algorithm
    if e.character_set:
        encoding_dict[convert_to_custom_property_name("character_set")] = e.character_set
    if e.custom_character_set_ref:
        encoding_dict[convert_to_custom_property_name("custom_character_set_ref")] = e.custom_character_set_ref
    return encoding_dict


def convert_artifact_packaging(packaging, instance, obj1x_id):
    if packaging.compression:
        if get_option_value("missing_policy") == "use-custom-properties":
            result = []
            for c in packaging.compression:
                result.append(convert_artifact_compression(c))
            instance[convert_to_custom_property_name("compression")] = result
        else:
            warn("Any artifact compression info on %s is not recoverable", 634, obj1x_id)
    if packaging.encoding:
        if get_option_value("missing_policy") == "use-custom-properties":
            result = []
            for e in packaging.encoding:
                result.append(convert_artifact_encoding(e))
            instance[convert_to_custom_property_name("encoding")] = result
        else:
            warn("Any artifact encoding info on %s is not recoverable", 634, obj1x_id)
    if packaging.encryption:
        first = True
        for e in packaging.encryption:
            if first:
                if e.encryption_key:
                    if get_option_value("spec_version") == "2.0":
                        property_name = convert_to_custom_property_name("encryption_key")
                    else:
                        property_name = "decryption_key"
                    instance[property_name] = e.encryption_key
                if e.encryption_mechanism:
                    if get_option_value("spec_version") == "2.0":
                        property_name = convert_to_custom_property_name("encryption_mechanism")
                    else:
                        property_name = "encryption_algorithm"
                    instance[property_name] = e.encryption_mechanism
                if e.encryption_key_ref:
                    handle_missing_string_property(instance, "encryption_key_ref", e.encryption_key_ref, is_sco=True)
                if e.encryption_mechanism_ref:
                    if get_option_value("missing_policy") == "use-custom-properties":
                        handle_missing_string_property(instance, "encryption_mechanism_ref", e.encryption_mechanism_ref, is_sco=True)
                first = False
            else:
                warn("Only one encryption algorithm or key allowed in STIX 2.1 - used first one in %s", 510, obj1x_id)


def convert_artifact(art, obj1x_id):
    instance = create_base_sco(art, "artifact")
    if art.content_type:
        instance["mime_type"] = art.content_type
    if art.raw_artifact:
        instance["payload_bin"] = art.raw_artifact.value
    if art.raw_artifact_reference:
        instance["url"] = art.raw_artifact_reference
    if art.hashes:
        instance["hashes"] = convert_hashes(art.hashes)
    if art.packaging:
        convert_artifact_packaging(art.packaging, instance, obj1x_id)

    finish_sco(instance, obj1x_id)
    return instance


def convert_uri(uri, obj1x_id):
    instance = create_base_sco(uri, "url", {"value": uri.value.value})
    finish_sco(instance, obj1x_id)
    return instance


def convert_hashes(hashes):
    hash_dict = {}
    for h in hashes:
        if getattr(h, "simple_hash_value"):
            hash_value = h.simple_hash_value
        else:
            hash_value = h.fuzzy_hash_value
        if text_type(h.type_).startswith("SHA"):
            hash_type = "'" + "SHA" + "-" + text_type(h.type_)[3:] + "'"
        elif text_type(h.type_) == "SSDEEP":
            hash_type = text_type(h.type_).lower()
        else:
            hash_type = text_type(h.type_)
        hash_dict[hash_type] = hash_value
    return hash_dict


_PE_FILE_HEADER_PROPERTY_MAP = \
    [["machine", "machine_hex"],
     ["time_date_stamp", "time_date_stamp"],
     ["number_of_sections", "number_of_sections"],
     ["pointer_to_symbol_table", "pointer_to_symbol_table"],
     ["number_of_symbols", "number_of_symbols"],
     ["size_of_optional_header", "size_of_optional_header"],
     ["characteristics", "characteristics_hex"]]

_PE_SECTION_HEADER_PROPERTY_MAP = \
    [["name", "name"],
     ["virtual_size", "size"]]


def convert_windows_executable_file(f):
    w_ex_dict = {}
    if f.headers:
        file_header = f.headers.file_header
        if file_header:
            for prop_tuple in _PE_FILE_HEADER_PROPERTY_MAP:
                prop_name1x = prop_tuple[0]
                prop_name2x = prop_tuple[1]
                if getattr(file_header, prop_name1x, None):
                    w_ex_dict[prop_name2x] = getattr(file_header, prop_name1x).value
            if file_header.hashes is not None:
                w_ex_dict["file_header_hashes"] = convert_hashes(file_header.hashes)
        if f.headers.optional_header:
            warn("file:extensions:'windows-pebinary-ext':optional_header is not implemented yet", 807)

    if f.type_:
        w_ex_dict["pe_type"] = map_vocabs_to_label(f.type_.value, WINDOWS_PEBINARY)
    sections = f.sections
    if sections:
        section_objs = []
        # should order matter in patterns???
        for s in sections:
            section_dict = {}
            if s.section_header:
                for prop_tuple in _PE_SECTION_HEADER_PROPERTY_MAP:
                    prop_name1x = prop_tuple[0]
                    prop_name2x = prop_tuple[1]
                    if getattr(s.section_header, prop_name1x, None):
                        section_dict[prop_name2x] = getattr(s.section_header, prop_name1x).value
            if s.entropy:
                if s.entropy.min:
                    handle_missing_string_property(section_dict, "entropy_min", s.entropy.min, is_sco=True)
                if s.entropy.max:
                    handle_missing_string_property(section_dict, "entropy_max", s.entropy.max, is_sco=True)
                if s.entropy.value:
                    section_dict["entropy"] = s.entropy.value.value
            # need to merge hash lists - worry about duplicate keys
            if s.data_hashes:
                section_dict["hashes"] = convert_hashes(s.data_hashes)
            if s.header_hashes:
                section_dict["hashes"] = convert_hashes(s.header_hashes)
            if section_dict:
                section_objs.append(section_dict)
        if section_objs:
            w_ex_dict["sections"] = section_objs
    if f.exports:
        warn("The exports property of WinExecutableFileObj is not part of STIX 2.x", 418)
    if f.imports:
        warn("The imports property of WinExecutableFileObj is not part of STIX 2.x", 418)
    return w_ex_dict


def convert_archive_file20(f, obj1x_id):
    index = 0
    archive_dict = dict()
    file_objs = dict()
    if f.comment:
        archive_dict["comment"] = f.comment
    if f.version:
        archive_dict["version"] = f.version
    if f.archived_file:
        archive_dict["contains_refs"] = list()
        for ar_file in f.archived_file:
            archive_dict["contains_refs"].append(text_type(index))
            ar_file2x, index = convert_file(ar_file, obj1x_id, index)
            file_objs.update(ar_file2x)
    return archive_dict, file_objs


def convert_archive_file21(f, obj1x_id):
    archive_dict = {}
    file_objs = []
    if f.comment:
        archive_dict["comment"] = f.comment
    if f.version:
        if get_option_value("missing_policy") == "use-custom-properties":
            property_name = convert_to_custom_property_name("version")
            archive_dict[property_name] = f.version
    if f.archived_file:
        for ar_file in f.archived_file:
            ar_file2x, ignore = convert_file(ar_file, obj1x_id)
            file_objs.extend(ar_file2x)
        archive_dict["contains_refs"] = [x["id"] for x in file_objs]
    return archive_dict, file_objs


_DIRECTORY_SCOS = {}


def add_to_directory_mapping(id, sco):
    global _DIRECTORY_SCOS
    _DIRECTORY_SCOS[id] = sco


def id_in_directory_mapping(id):
    return id in _DIRECTORY_SCOS


def get_sco_from_directory_mapping(id):
    return _DIRECTORY_SCOS[id]


def clear_directory_mappings():
    global _DIRECTORY_SCOS
    _DIRECTORY_SCOS = {}


_DIRECTORY_PATHS = {}


def add_to_directory_path_mapping(path, index):
    global _DIRECTORY_PATHS
    _DIRECTORY_PATHS[path] = index


def index_in_directory_path_mapping(path):
    return path in _DIRECTORY_PATHS


def get_index_from_directory_path_mapping(path):
    return _DIRECTORY_PATHS[path]


def clear_directory_path_mappings():
    global _DIRECTORY_PATHS
    _DIRECTORY_PATHS = {}


def convert_file_properties(f, obj1x_id):
    file_dict = create_base_sco(f, "file")
    extended_properties = {}
    dir_dict = None
    if f.size is not None:
        if isinstance(f.size.value, list):
            warn("File size 'window' not allowed in top level observable, using first value", 511)
            file_dict["size"] = int(f.size.value[0])
        else:
            file_dict["size"] = int(f.size)
    if f.created_time:
        if get_option_value("spec_version") == "2.0":
            file_dict["created"] = f.created_time
        else:
            file_dict["ctime"] = f.created_time
    if f.modified_time:
        if get_option_value("spec_version") == "2.0":
            file_dict["modified"] = f.modified_time
        else:
            file_dict["mtime"] = f.modified_time
    if f.accessed_time:
        if get_option_value("spec_version") == "2.0":
            file_dict["accessed"] = f.accessed_time
        else:
            file_dict["atime"] = f.accessed_time
    if f.hashes is not None:
        hashes = {}
        for h in f.hashes:
            if text_type(h.type_).startswith("SHA"):
                hash_type = "SHA" + "-" + text_type(h.type_)[3:]
            elif text_type(h.type_) == "SSDEEP":
                hash_type = text_type(h.type_).lower()
            else:
                hash_type = text_type(h.type_)
            hashes[hash_type] = h.simple_hash_value.value
        file_dict["hashes"] = hashes
    if f.file_name:
        file_dict["name"] = text_type(f.file_name)
        if f.file_extension:
            file_dict["name"] += "." + text_type(f.file_extension)
    elif f.file_path and f.file_path.value:
        # this index is an array index, not for the objects dict
        index = f.file_path.value.rfind("/")
        if index == -1:
            index = f.file_path.value.rfind("\\")
        if not (f.file_path.value.endswith("/") or f.file_path.value.endswith("\\")):
            file_dict["name"] = f.file_path.value[index + 1:]
        dir_path = f.file_path.value[0: index]
        if dir_path:
            full_path = f.device_path.value if f.device_path else ""
            dir_dict = create_base_sco(None, "directory", {"path": full_path + dir_path})
            finish_sco(dir_dict, None)
    if f.full_path:
        warn("1.x full file paths are not processed, yet", 802)
    if isinstance(f, WinExecutableFile):
        windows_executable_file_dict = convert_windows_executable_file(f)
        if windows_executable_file_dict:
            extended_properties["windows-pebinary-ext"] = windows_executable_file_dict
        else:
            warn("No WinExecutableFile properties found in %s", 613, text_type(f))
    if isinstance(f, ArchiveFile):
        if get_option_value("spec_version") == "2.0":
            archive_file_dict, file_objs = convert_archive_file20(f, obj1x_id)
        else:
            archive_file_dict, file_objs = convert_archive_file21(f, obj1x_id)
        if archive_file_dict:
            extended_properties["archive-ext"] = archive_file_dict
        else:
            warn("No ArchiveFile properties found in %s", 614, text_type(f))
    else:
        file_objs = None
    if extended_properties:
        file_dict["extensions"] = extended_properties
    finish_sco(file_dict, obj1x_id)
    return file_dict, dir_dict, file_objs


def convert_file20(f, obj1x_id, index=0):
    objs = {}
    file_obj_index = index
    objs[text_type(index)], dir_dict, file_objs = convert_file_properties(f, obj1x_id)
    if dir_dict:
        if index_in_directory_path_mapping(dir_dict["path"]):
            objs[text_type(index)]["parent_directory_ref"] = text_type(get_index_from_directory_path_mapping(dir_dict["path"]))
            index += 1
        else:
            objs[text_type(index + 1)] = dir_dict
            add_to_directory_path_mapping(dir_dict["path"], index + 1)
            objs[text_type(index)]["parent_directory_ref"] = text_type(index + 1)
            index += 2
    if file_objs:
        number_mapping = {}
        for k in sorted(file_objs.keys()):
            number_mapping[text_type(k)] = text_type(index)
            index += 1
        new_objs = renumber_objs(file_objs, number_mapping)
        objs.update(new_objs)
        renumber_co(objs[text_type(file_obj_index)], number_mapping)
    return objs, index


def convert_file21(f, obj1x_id):
    file_dict, dir_dict, file_objs = convert_file_properties(f, obj1x_id)
    objs = [file_dict]
    if dir_dict:
        objs.append(dir_dict)
        file_dict["parent_directory_ref"] = dir_dict["id"]
    if file_objs:
        for obj in file_objs:
            if not id_in_directory_mapping(obj["id"]):
                objs.append(obj)
                add_to_directory_mapping(dir_dict["id"], dir_dict)
    return objs


def convert_file(f, obj1x_id, index=0):
    if get_option_value("spec_version") == "2.0":
        return convert_file20(f, obj1x_id, index)
    else:
        return convert_file21(f, obj1x_id), None


def convert_attachment(attachment):
    info("content_type for body_multipart of attachment %s is assumed to be 'text/plain'", 722, attachment.object_reference)
    return {"body_raw_ref": attachment.object_reference, "content_type": "text/plain"}


def convert_email_message(email_message, obj1x_id):
    index = 0
    spec_version = get_option_value("spec_version")
    email_dict = create_base_sco(email_message, "email-message", {"is_multipart": False})  # the default
    if spec_version == "2.0":
        objs = dict()
        objs[text_type(index)] = email_dict
    else:
        objs = [email_dict]
    index += 1
    if email_message.header:
        header = email_message.header
        if header.date:
            email_dict["date"] = convert_timestamp_to_string(header.date)
        if header.content_type:
            email_dict["content_type"] = text_type(header.content_type)
        if header.subject:
            email_dict["subject"] = text_type(header.subject)
        if header.from_:
            # should there ever be more than one?
            from_ref = convert_address(header.from_)
            if spec_version == "2.0":
                objs[text_type(index)] = from_ref
            else:
                objs.append(from_ref)
            email_dict["from_ref"] = text_type(index) if spec_version == "2.0" else from_ref["id"]
            index += 1
        if header.to:
            for t in header.to:
                to_ref = convert_address(t)
                if spec_version == "2.0":
                    objs[text_type(index)] = to_ref
                else:
                    objs.append(to_ref)
                if "to_refs" not in email_dict:
                    email_dict["to_refs"] = []
                email_dict["to_refs"].append(text_type(index) if spec_version == "2.0" else to_ref["id"])
                index += 1
        if header.cc:
            for t in header.cc:
                cc_ref = convert_address(t)
                if spec_version == "2.0":
                    objs[text_type(index)] = cc_ref
                else:
                    objs.append(cc_ref)
                if "cc_refs" not in email_dict:
                    email_dict["cc_refs"] = []
                email_dict["cc_refs"].append(text_type(index) if spec_version == "2.0" else cc_ref["id"])
                index += 1
        if header.bcc:
            for t in header.bcc:
                bcc_ref = convert_address(t)
                if spec_version == "2.0":
                    objs[text_type(index)] = bcc_ref
                else:
                    objs.append(bcc_ref)
                if "bcc_refs" not in email_dict:
                    email_dict["bcc_refs"] = []
                email_dict["bcc_refs"].append(text_type(index) if spec_version == "2.0" else bcc_ref["id"])
                index += 1
        # TODO: handle additional headers
    if email_message.attachments:
        email_dict["is_multipart"] = True
        multiparts = []
        for a in email_message.attachments:
            multiparts.append(convert_attachment(a))
        email_dict["body_multipart"] = multiparts
    if email_message.links:
        if get_option_value("missing_policy") == "use-custom-properties":
            # this would be to another observable - which is not allowed in 2.0
            if get_option_value("spec_version") == "2.1":
                property_name = convert_to_custom_property_name("link_refs")
                email_dict[property_name] = list()
                for l in email_message.links:
                    sco_id = get_id_value(l.object_reference)
                    email_dict[property_name].append(sco_id)
                warn("Used custom property for %s", 308, "links")
            else:
                warn("Observed Data objects cannot refer to other external objects (in STIX 2.0): %s in %s",
                     434, "links", "email-message")
        else:
            warn("Missing property %s is ignored", 307, "links")
    finish_sco(email_dict, obj1x_id)
    return objs


def convert_registry_key(reg_key, obj1x_id):
    cybox_reg = create_base_sco(reg_key, "windows-registry-key")
    if reg_key.key or reg_key.hive:
        full_key = ""
        if reg_key.hive:
            full_key += reg_key.hive.value + "\\"
        if reg_key.key:
            full_key += reg_key.key.value
        cybox_reg["key"] = full_key
    else:
        error("windows-registry-key is required to have a key property", 608)
    if reg_key.values:
        cybox_reg["values"] = []
        for v in reg_key.values:
            reg_value = {}
            if hasattr(v, "data") and v.data:
                reg_value["data"] = text_type(v.data)
            if hasattr(v, "name") and v.name:
                reg_value["name"] = text_type(v.name)
            if hasattr(v, "datatype") and v.datatype:
                reg_value["data_type"] = text_type(v.datatype)
            cybox_reg["values"].append(reg_value)
    if reg_key.modified_time:
        if get_option_value("spec_version") == "2.0":
            cybox_reg["modified"] = convert_timestamp_to_string(reg_key.modified_time)
        else:
            cybox_reg["modified_time"] = convert_timestamp_to_string(reg_key.modified_time)
    finish_sco(cybox_reg, obj1x_id)
    return cybox_reg


def create_process_ref(cp, process_dict, objs, index, prop):
    spec_version = get_option_value("spec_version")
    cp_ref = create_base_sco(cp, "process", {"pid": cp.value})
    if get_option_value("spec_version") == "2.0":
        objs[text_type(index)] = cp_ref
    else:
        finish_sco(cp_ref, None)
        objs.append(cp_ref)
    if prop == "child_refs":
        if prop not in process_dict:
            process_dict["child_refs"] = []
        if spec_version == "2.0":
            process_dict[prop].append(text_type(index))
        else:
            process_dict[prop].append(cp_ref["id"])
    else:
        if spec_version == "2.0":
            process_dict[prop] = text_type(index)
        else:
            process_dict[prop] = cp_ref["id"]


def convert_port(prop, obj1x_id):
    traffic_2x = create_base_sco(prop, "network-traffic")
    if prop.port_value:
        warn("port number is assumed to be a destination port", 725)
        traffic_2x["dst_port"] = prop.port_value.value
    if prop.layer4_protocol:
        traffic_2x["protocols"] = [prop.layer4_protocol.value.lower()]
    finish_sco(traffic_2x, obj1x_id)
    return traffic_2x


def convert_opened_connection_refs20(process, process_dict, objs, index):
    renumbered_nc_dicts = {}
    process_dict["opened_connection_refs"] = []
    for nc in process.network_connection_list:
        nc_dicts = convert_network_connection(nc, None)
        root_obj_index = find_index_of_type(nc_dicts, "network-traffic")
        current_largest_id, number_mapping = do_renumbering(nc_dicts,
                                                            index,
                                                            root_obj_index,
                                                            renumbered_nc_dicts)
        objs.update(renumbered_nc_dicts)
        process_dict["opened_connection_refs"].append(text_type(number_mapping[root_obj_index]))
        index = current_largest_id
    return index


def convert_opened_connection_refs21(process, process_dict, objs):
    process_dict["opened_connection_refs"] = []
    for nc in process.network_connection_list:
        nc_dicts = convert_network_connection(nc, None)
        for obj in nc_dicts:
            objs.append(obj)
        # network-traffic is always the last obj
        process_dict["opened_connection_refs"].append(obj["id"])


def convert_process(process, obj1x_id):
    index = 0
    process_dict = create_base_sco(process, "process")
    if get_option_value("spec_version") == "2.0":
        objs = {}
        objs[text_type(index)] = process_dict
    else:
        objs = [process_dict]
    index += 1
    if process.name and get_option_value("spec_version") == "2.0":
        process_dict["name"] = text_type(process.name)
    if process.pid:
        process_dict["pid"] = process.pid.value
    if process.creation_time:
        process_dict["created" if get_option_value("spec_version") == "2.0" else "created_time"] = \
            convert_timestamp_to_string(process.creation_time.value)
    if process.argument_list and get_option_value("spec_version") == "2.0":
        process_dict["arguments"] = []
        for a in process.argument_list:
            process_dict["arguments"].append(a.value)
    if process.network_connection_list:
        if get_option_value("spec_version") == "2.0":
            index = convert_opened_connection_refs20(process, process_dict, objs, index)
        else:
            convert_opened_connection_refs21(process, process_dict, objs)
    if isinstance(process, WinProcess):
        extended_properties = dict()
        process_properties = convert_windows_process(process)
        if process_properties:
            extended_properties["windows-process-ext"] = process_properties
        if isinstance(process, WinService):
            service_properties, dll_file_obj = convert_windows_service(process)
            if service_properties:
                extended_properties["windows-service-ext"] = service_properties
            if dll_file_obj:
                if get_option_value("spec_version") == "2.0":
                    objs[text_type(index)] = dll_file_obj
                else:
                    objs.append(dll_file_obj)
                index += 1
        if extended_properties:
            process_dict["extensions"] = extended_properties
    finish_sco(process_dict, obj1x_id)
    if process.child_pid_list:
        for cp in process.child_pid_list:
            create_process_ref(cp, process_dict, objs, index, "child_refs")
            index += 1
    if process.parent_pid:
        create_process_ref(process.parent_pid, process_dict, objs, index, "parent_ref")
        index += 1
    return objs


def convert_windows_process(process):
    ext = {}
    if process.handle_list:
        for h in process.handle_list:
            warn("Windows handles are not a part of STIX 2.x", 420)
    if process.aslr_enabled:
        ext["asl_enabled"] = bool(process.aslr_enabled)
    if process.dep_enabled:
        ext["dep_enabled"] = bool(process.dep_enabled)
    if process.priority:
        ext["priority"] = text_type(process.priority)
    if process.security_id:
        ext["owner_sid"] = text_type(process.security_id)
    if process.window_title:
        ext["window_title"] = text_type(process.window_title)
    if process.startup_info:
        warn("CybOX object %s not handled yet not handled yet", 805, "process:startup_info")
    return ext


def convert_windows_service(service):
    cybox_ws = {}
    if hasattr(service, "service_name") and service.service_name:
        cybox_ws["service_name"] = service.service_name.value
    if hasattr(service, "description_list") and service.description_list:
        descriptions = []
        for d in service.description_list:
            descriptions.append(d.value)
        cybox_ws["descriptions"] = descriptions
    if hasattr(service, "display_name") and service.display_name:
        cybox_ws["display_name"] = service.display_name.value
    if hasattr(service, "startup_command_line") and service.startup_command_line:
        cybox_ws["startup_command_line"] = service.startup_command_line.value
    if hasattr(service, "startup_type") and service.startup_type:
        cybox_ws["start_type"] = map_vocabs_to_label(service.startup_type, SERVICE_START_TYPE)
    if hasattr(service, "service_type") and service.service_type:
        cybox_ws["service_type"] = map_vocabs_to_label(service.service_type, SERVICE_TYPE)
    if hasattr(service, "service_status") and service.service_status:
        cybox_ws["service_status"] = map_vocabs_to_label(service.service_status, SERVICE_STATUS)
    if hasattr(service, "service_dll") and service.service_dll:
        ddl_file2x = create_base_sco(None, "file", {"name": text_type(service.service_dll)})
        finish_sco(ddl_file2x, None)
        if get_option_value("spec_version") == "2.1":
            cybox_ws["service_dll_refs"] = [ddl_file2x["id"]]
        return cybox_ws, ddl_file2x
    return cybox_ws, None


def convert_domain_name(domain_name, obj1x_id):
    cybox_dm = create_base_sco(domain_name, "domain-name")
    if domain_name.value:
        cybox_dm["value"] = text_type(domain_name.value.value)

    # TODO: resolves_to_refs
    finish_sco(cybox_dm, obj1x_id)
    return cybox_dm


def convert_mutex(mutex, obj1x_id):
    cybox_mutex = create_base_sco(mutex, "mutex")
    if mutex.name:
        cybox_mutex["name"] = text_type(mutex.name.value)
    finish_sco(cybox_mutex, obj1x_id)
    return cybox_mutex


def convert_http_client_request(request):
    http_extension = {}

    if request.http_request_line is not None:
        if request.http_request_line.http_method is not None:
            http_extension["request_method"] = text_type(request.http_request_line.http_method.value.lower())
        if request.http_request_line.value is not None:
            http_extension["request_value"] = text_type(request.http_request_line.value.value.lower())
        if request.http_request_line.version is not None:
            http_extension["request_version"] = text_type(request.http_request_line.version.value.lower())

    if request.http_request_header is not None:
        if request.http_request_header.parsed_header is not None:
            header = {}
            if request.http_request_header.parsed_header.accept is not None:
                header["Accept"] = text_type(request.http_request_header.parsed_header.accept.value)
            if request.http_request_header.parsed_header.accept_charset is not None:
                header["Accept-Charset"] = text_type(request.http_request_header.parsed_header.accept_charset.value)
            if request.http_request_header.parsed_header.accept_language is not None:
                header["Accept-Language"] = text_type(request.http_request_header.parsed_header.accept_language.value)
            if request.http_request_header.parsed_header.accept_datetime is not None:
                header["Accept-Datetime"] = text_type(request.http_request_header.parsed_header.accept_datetime.value)
            if request.http_request_header.parsed_header.accept_encoding is not None:
                header["Accept-Encoding"] = text_type(request.http_request_header.parsed_header.accept_encoding.value)
            if request.http_request_header.parsed_header.authorization is not None:
                header["Authorization"] = text_type(request.http_request_header.parsed_header.authorization.value)
            if request.http_request_header.parsed_header.cache_control is not None:
                header["Cache-Control"] = text_type(request.http_request_header.parsed_header.cache_control.value)
            if request.http_request_header.parsed_header.connection is not None:
                header["Connection"] = text_type(request.http_request_header.parsed_header.connection.value)
            if request.http_request_header.parsed_header.cookie is not None:
                header["Cookie"] = text_type(request.http_request_header.parsed_header.cookie.value)
            if request.http_request_header.parsed_header.content_length is not None:
                header["Content-Length"] = text_type(request.http_request_header.parsed_header.content_length.value)
            if request.http_request_header.parsed_header.content_md5 is not None:
                header["Content-MD5"] = text_type(request.http_request_header.parsed_header.content_md5.value)
            if request.http_request_header.parsed_header.content_type is not None:
                header["Content-Type"] = text_type(request.http_request_header.parsed_header.content_type.value)
            if request.http_request_header.parsed_header.date is not None:
                header["Date"] = text_type(request.http_request_header.parsed_header.date)
            if request.http_request_header.parsed_header.expect is not None:
                header["Expect"] = text_type(request.http_request_header.parsed_header.expect.value)
            if request.http_request_header.parsed_header.from_ is not None:
                from_ = request.http_request_header.parsed_header.from_
                if from_.address_value is not None:
                    header["From"] = text_type(from_.address_value.value)
            if request.http_request_header.parsed_header.host is not None:
                host = request.http_request_header.parsed_header.host
                value = ""
                has_domain = False
                if host.domain_name is not None:
                    has_domain = True
                    value += text_type(host.domain_name.value)
                if host.port is not None:
                    if has_domain:
                        value += ":" + text_type(host.port.port_value)
                    else:
                        value += text_type(host.port.port_value)
                if value:
                    header["Host"] = value
            if request.http_request_header.parsed_header.if_match is not None:
                header["If-Match"] = text_type(request.http_request_header.parsed_header.if_match.value)
            if request.http_request_header.parsed_header.if_modified_since is not None:
                header["If-Modified-Since"] = text_type(
                    request.http_request_header.parsed_header.if_modified_since.value)
            if request.http_request_header.parsed_header.if_none_match is not None:
                header["If-None-Match"] = text_type(request.http_request_header.parsed_header.if_none_match.value)
            if request.http_request_header.parsed_header.if_range is not None:
                header["If-Range"] = text_type(request.http_request_header.parsed_header.if_range.value)
            if request.http_request_header.parsed_header.if_unmodified_since is not None:
                header["If-Unmodified-Since"] = text_type(
                    request.http_request_header.parsed_header.if_unmodified_since.value)
            if request.http_request_header.parsed_header.max_forwards is not None:
                header["Max-Forwards"] = text_type(request.http_request_header.parsed_header.max_forwards.value)
            if request.http_request_header.parsed_header.pragma is not None:
                header["Pragma"] = text_type(request.http_request_header.parsed_header.pragma.value)
            if request.http_request_header.parsed_header.proxy_authorization is not None:
                header["Proxy-Authorization"] = text_type(
                    request.http_request_header.parsed_header.proxy_authorization.value)
            if request.http_request_header.parsed_header.range_ is not None:
                header["Range"] = text_type(request.http_request_header.parsed_header.range_.value)
            if request.http_request_header.parsed_header.referer is not None:
                header["Referer"] = text_type(request.http_request_header.parsed_header.referer.value)
            if request.http_request_header.parsed_header.te is not None:
                header["TE"] = text_type(request.http_request_header.parsed_header.te.value)
            if request.http_request_header.parsed_header.user_agent is not None:
                header["User-Agent"] = text_type(request.http_request_header.parsed_header.user_agent.value)
            if request.http_request_header.parsed_header.via is not None:
                header["Via"] = text_type(request.http_request_header.parsed_header.via.value)
            if request.http_request_header.parsed_header.warning is not None:
                header["Warning"] = text_type(request.http_request_header.parsed_header.warning.value)
            if request.http_request_header.parsed_header.dnt is not None:
                header["DNT"] = text_type(request.http_request_header.parsed_header.dnt.value)
            if request.http_request_header.parsed_header.x_requested_with is not None:
                header["X-Requested-With"] = text_type(request.http_request_header.parsed_header.x_requested_with.value)
            if request.http_request_header.parsed_header.x_forwarded_for is not None:
                header["X-Forwarded-For"] = text_type(request.http_request_header.parsed_header.x_forwarded_for.value)
            if request.http_request_header.parsed_header.x_att_deviceid is not None:
                header["X-ATT-DeviceId"] = text_type(request.http_request_header.parsed_header.x_att_deviceid.value)
            if request.http_request_header.parsed_header.x_wap_profile is not None:
                header["X-Wap-Profile"] = text_type(request.http_request_header.parsed_header.x_wap_profile.value)

            http_extension["request_header"] = header
            # http_extension["request_value"]
            # http_extension["message_body_length"]
            # http_extension["message_body_data_length"]
            return http_extension


def convert_http_network_connection_extension(http):
    if http is not None:
        return convert_http_client_request(http.http_client_request)


def convert_network_connection(conn, obj1x_id):
    index = 0
    spec_version = get_option_value("spec_version")
    cybox_traffic = {}
    if spec_version == "2.0":
        objs = {}
    else:
        objs = []

    def create_domain_name_object(dn, obj1x_id):
        instance = create_base_sco(None, "domain-name", {"value": text_type(dn.value)})
        finish_sco(instance, obj1x_id)
        return instance

    if conn.creation_time is not None:
        cybox_traffic["start"] = convert_timestamp_to_string(conn.creation_time.value, None, None)

    cybox_traffic["protocols"] = []

    if conn.layer3_protocol is not None:
        cybox_traffic["protocols"].append(text_type(conn.layer3_protocol.value).lower())

    if conn.source_socket_address is not None:
        # The source, if present will have index "0".
        if conn.source_socket_address.port is not None:
            if conn.source_socket_address.port.port_value is not None:
                cybox_traffic["src_port"] = int(conn.source_socket_address.port.port_value)
            if conn.source_socket_address.port.layer4_protocol is not None:
                cybox_traffic["protocols"].append(text_type(conn.source_socket_address.port.layer4_protocol.value.lower()))
        if conn.source_socket_address.ip_address is not None:
            source = convert_address(conn.source_socket_address.ip_address)
            cybox_traffic["src_ref"] = str(index) if spec_version == "2.0" else source["id"]
            if spec_version == "2.0":
                objs[text_type(index)] = source
            else:
                objs.append(source)
            index += 1
        elif conn.source_socket_address.hostname is not None:
            if conn.source_socket_address.hostname.is_domain_name and conn.source_socket_address.hostname.hostname_value is not None:
                source_domain = create_domain_name_object(conn.source_socket_address.hostname.hostname_value, None)
                cybox_traffic["src_ref"] = str(index) if spec_version == "2.0" else source_domain["id"]
                if spec_version == "2.0":
                    objs[text_type(index)] = source_domain
                else:
                    objs.append(source_domain)
                index += 1
            elif (conn.source_socket_address.hostname.naming_system is not None and
                    any(x.value == "DNS" for x in conn.source_socket_address.hostname.naming_system)):
                source_domain = create_domain_name_object(conn.source_socket_address.hostname.hostname_value, None)
                cybox_traffic["src_ref"] = str(index) if spec_version == "2.0" else source_domain["id"]
                if spec_version == "2.0":
                    objs[text_type(index)] = source_domain
                else:
                    objs.append(source_domain)
                index += 1

    if conn.destination_socket_address is not None:
        # The destination will have index "1" if there is a source.
        if conn.destination_socket_address.port is not None:
            if conn.destination_socket_address.port is not None:
                cybox_traffic["dst_port"] = int(conn.destination_socket_address.port.port_value)
            if conn.destination_socket_address.port.layer4_protocol is not None:
                cybox_traffic["protocols"].append(text_type(conn.destination_socket_address.port.layer4_protocol.value.lower()))
        if conn.destination_socket_address.ip_address is not None:
            destination = convert_address(conn.destination_socket_address.ip_address)
            cybox_traffic["dst_ref"] = str(index) if spec_version == "2.0" else destination["id"]
            if spec_version == "2.0":
                objs[text_type(index)] = destination
            else:
                objs.append(destination)
            index += 1
        elif conn.destination_socket_address.hostname is not None:
            if conn.destination_socket_address.hostname.is_domain_name and conn.destination_socket_address.hostname.hostname_value is not None:
                destination_domain = create_domain_name_object(conn.destination_socket_address.hostname.hostname_value, None)
                cybox_traffic["dst_ref"] = str(index) if spec_version == "2.0" else destination_domain["id"]
                if spec_version == "2.0":
                    objs[text_type(index)] = destination_domain
                else:
                    objs.append(destination_domain)
                index += 1
            elif (conn.destination_socket_address.hostname.naming_system is not None and
                    any(x.value == "DNS" for x in conn.destination_socket_address.hostname.naming_system)):
                destination_domain = create_domain_name_object(conn.destination_socket_address.hostname.hostname_value, None)
                cybox_traffic["dst_ref"] = str(index) if spec_version == "2.0" else destination_domain["id"]
                if spec_version == "2.0":
                    objs[text_type(index)] = destination_domain
                else:
                    objs.append(destination_domain)
                index += 1

    if conn.layer4_protocol is not None:
        cybox_traffic["protocols"].append(text_type(conn.layer4_protocol.value).lower())

    if conn.layer7_protocol is not None:
        cybox_traffic["protocols"].append(text_type(conn.layer7_protocol.value).lower())

    if conn.layer7_connections is not None:
        if conn.layer7_connections.http_session is not None:
            # HTTP extension
            cybox_traffic["extensions"] = {}
            request_responses = conn.layer7_connections.http_session.http_request_response
            if request_responses:
                cybox_traffic["extensions"] = {
                    "http-request-ext": convert_http_network_connection_extension(request_responses[0])}
                if len(conn.layer7_connections.http_session.http_request_response) > 1:
                    warn("Only one HTTP_Request_Response used for http-request-ext, using first value", 512)
        if conn.layer7_connections.dns_query:
            warn("Layer7_Connections/DNS_Query content not supported in STIX 2.x", 424)

    if cybox_traffic:
        cybox_traffic["type"] = "network-traffic"
        if spec_version == "2.0":
            objs[text_type(index)] = cybox_traffic
        else:
            finish_sco(cybox_traffic, obj1x_id)
            objs.append(cybox_traffic)

    # cybox_traffic["end"]
    # cybox_traffic["is_active"]
    # cybox_traffic["src_byte_count"]
    # cybox_traffic["dst_byte_count"]
    # cybox_traffic["src_packets"]
    # cybox_traffic["dst_packets"]
    # cybox_traffic["ipfix"]
    # cybox_traffic["src_payload_ref"]
    # cybox_traffic["dst_payload_ref"]
    # cybox_traffic["encapsulates_refs"]
    # cybox_traffic["encapsulated_by_ref"]

    return objs


def split_into_requests_and_responses(req_resp_list):
    requests = []
    responses = []
    for r in req_resp_list:
        if r.http_client_request:
            requests.append(r.http_client_request)
        if r.http_server_response:
            responses.append(r.http_server_response)
    return requests, responses


def convert_http_session(session, obj1x_id):
    if session.http_request_response:
        requests, responses = split_into_requests_and_responses(session.http_request_response)
        if len(responses) != 0:
            warn("HTTPServerResponse type is not supported in STIX 2.x", 429)
        if len(requests) >= 1:
            cybox_traffic = create_base_sco(requests[0], "network-traffic")
            cybox_traffic["extensions"] = {"http-request-ext": convert_http_client_request(requests[0])}
            if len(requests) > 1:
                warn("Only HTTP_Request_Response used for http-request-ext, using first value", 512)
            finish_sco(cybox_traffic, obj1x_id)
            return cybox_traffic


def create_icmp_extension(icmp_header):
    imcp_extension = {}
    if icmp_header.type_:
        imcp_extension["icmp_type_hex"] = icmp_header.type_.value
    if icmp_header.code:
        imcp_extension["icmp_code_hex"] = icmp_header.code.value
    if icmp_header.checksum:
        handle_missing_string_property(imcp_extension, "checksum", icmp_header.checksum, is_sco=True)
    return imcp_extension


def convert_network_packet(packet, obj1x_id):
    if packet.internet_layer:
        internet_layer = packet.internet_layer
        if internet_layer.ipv4 or internet_layer.ipv6:
            warn("Internet_Layer/IP_Packet content not supported in STIX 2.x", 424)
        else:
            if internet_layer.icmpv4:
                icmp_header = internet_layer.icmpv4.icmpv4_header
            elif internet_layer.icmpv6:
                icmp_header = internet_layer.icmpv6.icmpv6_header
            else:
                return None
            cybox_traffic = create_base_sco(packet, "network-traffic")
            cybox_traffic["extensions"] = {"icmp-ext": create_icmp_extension(icmp_header)}
            finish_sco(cybox_traffic, obj1x_id)
            return cybox_traffic


def convert_socket_options(options):
    socket_options = {}
    for prop_name in SOCKET_OPTIONS:
        if getattr(options, prop_name):
            socket_options[prop_name.upper()] = getattr(options, prop_name)
    return socket_options


def convert_network_socket(socket, obj1x_id):
    cybox_traffic = create_base_sco(socket, "network-traffic")
    socket_extension = {}
    if socket.is_blocking:
        socket_extension["is_blocking"] = socket.is_blocking
    if socket.is_listening:
        socket_extension["is_listening"] = socket.is_listening
    if socket.address_family:
        if socket.address_family in ADDRESS_FAMILY_ENUMERATION:
            socket_extension["address_family"] = socket.address_family.value
        else:
            warn("%s is not a member of the %s enumeration", 627, socket.address_family, "address family")
    if socket.type_:
        socket_extension["socket_type"] = socket.type_
    if socket.domain:
        if get_option_value("spec_version") == "2.0":
            socket_extension["protocol_family"] = socket.domain
        else:
            handle_missing_string_property(socket_extension, "protocol_family", socket.domain, is_sco=True)
    if socket.options:
        socket_extension["options"] = convert_socket_options(socket.options)
    if socket.socket_descriptor:
        socket_extension["socket_descriptor"] = socket.socket_descriptor
    if socket.local_address:
        handle_missing_string_property(socket_extension, "local_address", socket.local_address.ip_address, is_sco=True)
    if socket.remote_address:
        handle_missing_string_property(socket_extension, "remote_address", socket.remote_address.ip_address, is_sco=True)
    if socket.protocol:
        cybox_traffic["protocols"] = [socket.protocol.value.lower()]
    cybox_traffic["extensions"] = {"socket-ext": socket_extension}
    finish_sco(cybox_traffic, obj1x_id)
    return cybox_traffic


def convert_cybox_object20(obj1x):
    # in 2.0 indices are local
    clear_directory_path_mappings()
    # TODO:  should related objects be handled on a case-by-case basis or just ignored
    prop = obj1x.properties
    objs = {}
    if prop is None:
        return None
    elif isinstance(prop, Address):
        objs["0"] = convert_address(prop, obj1x.id_)
    elif isinstance(prop, Artifact):
        objs["0"] = convert_artifact(prop, obj1x.id_)
    elif isinstance(prop, URI):
        objs["0"] = convert_uri(prop, obj1x.id_)
    elif isinstance(prop, EmailMessage):
        # potentially returns multiple objects
        objs = convert_email_message(prop, obj1x.id_)
    elif isinstance(prop, File):
        # potentially returns multiple objects
        objs, ignore = convert_file20(prop, obj1x.id_)
    elif isinstance(prop, WinRegistryKey):
        objs["0"] = convert_registry_key(prop, obj1x.id_)
    elif isinstance(prop, Process):
        objs = convert_process(prop, obj1x.id_)
    elif isinstance(prop, DomainName):
        objs["0"] = convert_domain_name(prop, obj1x.id_)
    elif isinstance(prop, Mutex):
        objs["0"] = convert_mutex(prop, obj1x.id_)
    elif isinstance(prop, NetworkConnection):
        # potentially returns multiple objects
        objs = convert_network_connection(prop, obj1x.id_)
    elif isinstance(prop, Account):
        objs["0"] = convert_account(prop, obj1x.id_)
    elif isinstance(prop, Port):
        objs["0"] = convert_port(prop, obj1x.id_)
    elif isinstance(prop, HTTPSession):
        objs["0"] = convert_http_session(prop, obj1x.id_)
    elif isinstance(prop, NetworkPacket):
        objs["0"] = convert_network_packet(prop, obj1x.id_)
    elif isinstance(prop, NetworkSocket):
        objs["0"] = convert_network_socket(prop, obj1x.id_)
    else:
        warn("CybOX object %s not handled yet", 805, text_type(type(prop)))
        return None
    if not objs:
        warn("%s did not yield any STIX 2.x object", 417, text_type(type(prop)))
        return None
    else:
        primary_obj = objs["0"]
        if prop.custom_properties:
            for cp in prop.custom_properties.property_:
                primary_obj["x_" + cp.name] = cp.value
        if obj1x.id_:
            add_object_id_value(obj1x.id_, objs)
        return objs


def convert_cybox_object21(obj1x):
    # TODO:  should related objects be handled on a case-by-case basis or just ignored
    prop = obj1x.properties
    if prop is None:
        return None
    elif isinstance(prop, Address):
        objs = [convert_address(prop, obj1x.id_)]
    elif isinstance(prop, Artifact):
        objs = [convert_artifact(prop, obj1x.id_)]
    elif isinstance(prop, URI):
        objs = [convert_uri(prop, obj1x.id_)]
    elif isinstance(prop, EmailMessage):
        # potentially returns multiple objects
        objs = convert_email_message(prop, obj1x.id_)
    elif isinstance(prop, File):
        # potentially returns multiple objects
        objs = convert_file21(prop, obj1x.id_)
    elif isinstance(prop, WinRegistryKey):
        objs = [convert_registry_key(prop, obj1x.id_)]
    elif isinstance(prop, Process):
        objs = convert_process(prop, obj1x.id_)
    elif isinstance(prop, DomainName):
        objs = [convert_domain_name(prop, obj1x.id_)]
    elif isinstance(prop, Mutex):
        objs = [convert_mutex(prop, obj1x.id_)]
    elif isinstance(prop, NetworkConnection):
        # potentially returns multiple objects
        objs = convert_network_connection(prop, obj1x.id_)
    elif isinstance(prop, Account):
        objs = [convert_account(prop, obj1x.id_)]
    elif isinstance(prop, Port):
        objs = [convert_port(prop, obj1x.id_)]
    elif isinstance(prop, HTTPSession):
        objs = [convert_http_session(prop, obj1x.id_)]
    elif isinstance(prop, NetworkPacket):
        objs = [convert_network_packet(prop, obj1x.id_)]
    elif isinstance(prop, NetworkSocket):
        objs = [convert_network_socket(prop, obj1x.id_)]
    else:
        warn("CybOX object %s not handled yet", 805, text_type(type(prop)))
        return None
    if not objs:
        warn("%s did not yield any STIX 2.x object", 417, text_type(type(prop)))
        return None
    else:
        primary_obj = objs[0]
        if prop.custom_properties:
            for cp in prop.custom_properties.property_:
                primary_obj[convert_to_custom_property_name(cp.name)] = cp.value
        if obj1x.id_:
            add_object_id_value(obj1x.id_, objs)
        return objs


def find_index_of_type(objs, type):
    for k, v in objs.items():
        if v["type"] == type:
            return k
    return None


def renumber_co(co, number_mapping):
    for k, v in co.items():
        if k.endswith("ref"):
            if co[k] in number_mapping:
                co[k] = number_mapping[co[k]]
        elif k.endswith("refs"):
            new_refs = []
            for ref in co[k]:
                if ref in number_mapping:
                    new_refs.append(number_mapping[ref])
            co[k] = new_refs
        elif k == "extensions":
            for ex_k, ex_v in v.items():
                renumber_co(ex_v, number_mapping)
    return co


def renumber_objs(objs, number_mapping):

    new_objects = {}
    for k, v in objs.items():
        new_objects[number_mapping[k]] = renumber_co(v, number_mapping)
    return new_objects


def do_renumbering(objs, next_id, root_obj_index, objs_to_add):
    number_mapping = {}
    for k in sorted(objs.keys()):
        number_mapping[text_type(k)] = text_type(next_id)
        next_id += 1
    new_objs = renumber_objs(objs, number_mapping)
    objs_to_add.update(new_objs)
    return next_id, number_mapping


def find_index_of_contents(root_data, objects):
    for index, value in objects.items():
        if value == root_data:
            return index
    return None


def fix_cybox_relationships(observed_data):
    for o in observed_data:
        if not o["objects"]:
            continue
        objs_to_add = {}
        next_id = int(max(o["objects"].keys())) + 1
        for co in o["objects"].values():
            if co["type"] == "email-message":
                if co["is_multipart"]:
                    for mp in co["body_multipart"]:
                        objs = get_object_id_value(mp["body_raw_ref"])
                        if objs:
                            root_obj_index = find_index_of_type(objs, "file")
                            if root_obj_index is not None:  # 0 is a good value
                                mp["content_type"] = "text/plain"
                                info("content_type for body_multipart of %s is assumed to be 'text/plain'", 722,
                                     o["id"])
                                root_data = objs[root_obj_index]
                                if root_data:
                                    present_obj_index = find_index_of_contents(root_data, o["objects"])
                                    if present_obj_index is None:  # 0 is a good value
                                        next_id, number_mapping = do_renumbering(objs,
                                                                                 next_id,
                                                                                 root_obj_index,
                                                                                 objs_to_add)
                                        mp["body_raw_ref"] = text_type(number_mapping[root_obj_index])
                                    else:
                                        mp["body_raw_ref"] = text_type(present_obj_index)
                    # TODO: warnings
        if objs_to_add:
            o["objects"].update(objs_to_add)


def fix_attachments_refs(objects):
    for obj in objects:
        if obj["type"] == "email-message":
            if obj["is_multipart"]:
                for mp in obj["body_multipart"]:
                    mp["body_raw_ref"] = get_id_value(mp["body_raw_ref"])[0]
                    mp["content_type"] = "text/plain"
                    info("content_type for body_multipart of %s is assumed to be 'text/plain'", 722, obj["id"])
