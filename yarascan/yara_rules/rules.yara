rule dummy_rule
{
    strings:
        $a = "dummy"
    condition:
        $a
}
