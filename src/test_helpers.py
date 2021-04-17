import helpers

def test_formatTitle_exists():
    helpers.formatTitle('')

def test_formatTitle_returns_string():
    assert type(helpers.formatTitle('')) == type('')

def test_formatTitle_basic_format():
    title = 'measurement,tag,subtag'
    solution = 'measurement,tag=tag,subtag=subtag'
    assert helpers.formatTitle(title) == solution

    title = 'temp,sensor,water'
    solution = 'temp,tag=sensor,subtag=water'
    assert helpers.formatTitle(title) == solution

def test_formatTitle_underscore():
    title = 'temp,water sensor,water'
    solution = 'temp,tag=water_sensor,subtag=water'
    assert helpers.formatTitle(title) == solution

def test_formatTitle_short_input():
    title = 'temp,sensor'
    solution = 'temp,tag=sensor'
    assert helpers.formatTitle(title) == solution
