from md2pt_jp.converter import convert_markdown_to_plaintext

def test_markdown_to_plaintext_heading_and_bold():
    input_text = "###見出し３\n涼子のテレキネシスが**暴発**した"
    expected_output = "見出し３\n涼子のテレキネシスが暴発した"
    assert convert_markdown_to_plaintext(input_text) == expected_output
