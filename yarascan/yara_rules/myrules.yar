rule ExampleRule
{
    meta:
        description = "Detects the string 'malware'"
        author = "Your Name"
        date = "2024-07-04"
    strings:
        $a = "malware"
    condition:
        $a
}
rule test_rule {
    strings:
        $a = "test_string"
    condition:
        $a
}
rule zeus_cfg {
    strings:
        $a = "Zeus.cfg"
    condition:
        $a
}

rule stuxnet {
    strings:
        $a = "Stuxnet"
    condition:
        $a
}

rule emotet_malware_pattern {
    strings:
        $a = "Emotet malware pattern"
    condition:
        $a
}

rule locky_ransomware_pattern {
    strings:
        $a = "Locky Ransomware pattern"
    condition:
        $a 
}

rule zeus_banking_trojan {
    strings:
        $a = "Zeus Banking Trojan"
    condition:
        $a
}

rule malware_behavior1 {
    strings:
        $a = "malware_behavior1"
    condition:
        $a
}

rule malware_behavior2 {
    strings:
        $a = "malware_behavior2"
    condition:
        $a
}

rule process_cmd_modify_system32 {
    strings:
        $a = "Process 'cmd.exe' attempting to modify 'system32' files"
    condition:
        $a
}
