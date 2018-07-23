import pytest
from wallet import InsufficientAmount, Wallet, InsufficientFundsException, Banker, Customer


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


@pytest.fixture
def empty_banker():
    '''Returns a Banker instance with a zero balance'''
    return Banker()


@pytest.fixture
def empty_customer():
    '''Returns a User instance with a zero balance'''
    return Customer()


@pytest.fixture
def customer():
    '''Returns a User instance with a zero balance'''
    return Customer(10000)


@pytest.fixture
def banker():
    '''Returns a Banker instance with a balance of 20'''
    return Banker(10000)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
    (500, 400, 100)
])
def test_transaction(earned, spent, expected, empty_wallet):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


def test_initialBalance(empty_banker):
    assert empty_banker.total == 0


def test_giveLoan_within_limit(banker):
    banker.giveLoan(10000)
    assert banker.total == 0


def test_collectLoan(banker):
    banker.collectLoanAmount(1000)
    assert banker.total == 11000


def test_giveLoan_morethan_limit(banker):
    with pytest.raises(InsufficientFundsException):
        banker.giveLoan(11000)


def test_updateBalance(empty_customer):
    assert empty_customer.balance == 0


def test_updateBalance(customer):
    customer.updateBalance(10000)
    assert customer.balance == 20000


def test_payloanAmountwithbalance(customer):
    customer.payloanAmount(10000)
    assert customer.balance == 0

@pytest.mark.parametrize("loangivenamount,repaidloanamount,finalbalance", [
    (3000, 1000, 12000),
    (2000, 200, 11800),
    (5000, 4000, 11000)
])
def test_loanprocess(loangivenamount,repaidloanamount,finalbalance, customer):
    customer.updateBalance(loangivenamount)
    customer.payloanAmount(repaidloanamount)
    assert customer.balance == finalbalance