import requests
import json
import urllib.parse
import time


class Freee():
    def __init__(self, client_id, client_secret, company_id, token_filename):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_filename = token_filename
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.authorize_api_url = 'https://accounts.secure.freee.co.jp/public_api/token'
        self.account_endpoint = "https://api.freee.co.jp/api/1/"
        self.hr_endpoint = "https://api.freee.co.jp/hr/api/v1/"
        self.company_id = company_id

# ===========================================
#     認証系
# ===========================================

    def save_tokens(self, token_dict):
        f = open(self.token_filename, "w")
        json.dump(token_dict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

    def read_tokens(self):
        with open(self.token_filename) as f:
            return json.load(f)

    def get_access_token(self, authorization_code):
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': authorization_code,
            'redirect_uri': self.redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        res = requests.post(self.authorize_api_url, params=params, headers=headers)
        if res.ok:
            self.save_tokens(res.json())
        else:
            print("client_id, client_secret, authorization_codeのいずれかに不備がある可能性があります。再度認証コードを取得してください")
            raise res.raise_for_status()

    def set_tokens(self, token_dict):
        self.access_token = token_dict["access_token"]
        self.access_token_expired_at = token_dict["created_at"] + token_dict["expires_in"]
        self.refresh_token = token_dict["refresh_token"]

    def run_refresh_token(self):
        params = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token
        }
        res = requests.post(self.authorize_api_url, data=params)
        if res.ok:
            token_dict = res.json()
            self.set_tokens(token_dict)
            self.save_tokens(token_dict)
        else:
            print("client_id, client_secret, refresh_tokenのいずれかに不備がある可能性があります")
            raise res.raise_for_status()

# ===========================================
#     リクエスト系
# ===========================================

    def confirm_expired(self):
        return True if time.time() - self.access_token_expired_at >= 0 else False

    def send_request(self, request_method, url, payload):
        if self.confirm_expired():
            self.run_refresh_token()
        if request_method == "get":
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token
            }
            res = requests.get(url, headers=headers, params=payload)
            if res.ok:
                return res.json()
            else:
                raise res.raise_for_status()
        elif request_method == "put":
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token
            }
            res = requests.put(url, headers=headers, data=json.dumps(payload))
            if res.ok:
                return res.json()
            else:
                raise res.raise_for_status()
        elif request_method == "delete":
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token
            }
            res = requests.delete(url, headers=headers, data=json.dumps(payload))
            if res.ok:
                return res
            else:
                raise res.raise_for_status()


# ===========================================
#     会計freee API
# ===========================================


# ===========================================
#     Account items(勘定科目)
# ===========================================

    def get_account_item(self, account_item_id, **payload):

        """指定した勘定科目の詳細を取得

        指定した勘定科目の詳細を取得する

        Args:
            account_item_id (int): 勘定科目ID
            company_id (int): 事務所ID

        Returns:
            dict: like below
            {
              "account_item": {
                "id": 1,
                "name": "ソフトウェア",
                "company_id": 1,
                "tax_code": 1,
                "account_category_id": 1,
                "shortcut": "SOFUTO",
                "shortcut_num": "123",
                "corresponding_type_expense": 5,
                "corresponding_type_income": 2,
                "searchable": 2,
                "accumulated_dep_account_item_name": "減価償却累計額",
                "items": [
                  {
                    "name": "住民税",
                    "id": 1
                  }
                ],
                "partners": [
                  {
                    "name": "test",
                    "id": 1
                  }
                ],
                "available": true
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["account_items", str(account_item_id)]))
        return self.send_request(request_method, url, payload)

    def get_account_items(self, **payload):

        """ 勘定科目一覧の取得

        指定した事業所の勘定科目一覧を取得する

        Args:
            company_id (int): 事務所ID
            base_date (str, optional): 基準日:指定した場合、勘定科目に紐づく税区分(default_tax_code)が、基準日の税率に基づいて返ります。

        Returns:
            dict: like below
            {
              "account_items": [
                {
                  "id": 1,
                  "name": "ソフトウェア",
                  "default_tax_id": 34,
                  "default_tax_code": 34,
                  "categories": [
                    "資産"
                  ],
                  "available": true
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "account_items")
        return self.send_request(request_method, url, payload)

# ===========================================
#     Banks (連携サービス)
# ===========================================

# ===========================================
#     Companies(事務所)
# ===========================================

    def get_companies(self, **payload):
        """事業所一覧の取得

        事業所一覧の取得

        Args:
            No parameters

        Returns:
            dict: like below
            {
              "account_item": {
                "id": 1,
                "name": "ソフトウェア",
                "company_id": 1,
                "tax_code": 1,
                "account_category_id": 1,
                "shortcut": "SOFUTO",
                "shortcut_num": "123",
                "corresponding_type_expense": 5,
                "corresponding_type_income": 2,
                "searchable": 2,
                "accumulated_dep_account_item_name": "減価償却累計額",
                "items": [
                  {
                    "name": "住民税",
                    "id": 1
                  }
                ],
                "partners": [
                  {
                    "name": "test",
                    "id": 1
                  }
                ],
                "available": true
              }
            }

        Notes:
            定義
            role
                admin : 管理者
                simple_accounting : 一般
                self_only : 取引登録のみ
                read_only : 閲覧のみ
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "companies")
        return self.send_request(request_method, url, payload)

    def get_company(self, company_id, **payload):
        """事業所の詳細情報の取得

        ユーザが所属する事業所の詳細を取得する

        Args:
            id (int): 事業所ID
            details (bool): 取得情報に勘定科目・税区分コード・税区分・品目・取引先・部門・メモタグ・口座の一覧を含める. Available values : true
            account_items (bool): 取得情報に勘定科目一覧を含める. Available values : true
            taxes (bool): 取得情報に税区分コード・税区分一覧を含める. Available values : true
            items (bool): 取得情報に品目一覧を含める. Available values : true
            partners (bool): 取得情報に取引先一覧を含める. Available values : true
            sections (bool): 取得情報に部門一覧を含める. Available values : true
            tags (bool): 取得情報にメモタグ一覧を含める. Available values : true
            walletables (bool): 取得情報に口座一覧を含める. Available values : true


        Returns:
            dict: like below
            {
              "company": {
                "id": 1,
                "display_name": "freee事務所",
                "tax_at_source_calc_type": 0,
                "corporate_number": "1234567890123",
                "txn_number_format": "not_used",
                "default_wallet_account_id": 1,
                "private_settlement": true,
                "minus_format": 0,
                "role": "admin",
                "phone1": "03-1234-xxxx",
                "zipcode": "000-0000",
                "prefecture_code": 4,
                "street_name1": "ＸＸ区ＹＹ１−１−１",
                "street_name2": "ビル１Ｆ",
                "invoice_layout": 0,
                "invoice_style": 0,
                "amount_fraction": 0,
                "industry_class": "agriculture_forestry_fisheries_ore",
                "industry_code": "transport_delivery",
                "workflow_setting": "disabled",
                "use_partner_code": true
              }
            }

        Notes:
            定義
            role
                admin : 管理者
                simple_accounting : 一般
                self_only : 取引登録のみ
                read_only : 閲覧のみ
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["companies", str(company_id)]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     Deals(取引(収入/支出))
# ===========================================
    def get_deals(self, **payload):

        """取引一覧（収入／支出）の取得

        指定した事業所の取引一覧（収入／支出）を取得する

        Args:
            company_id (int): 事務所ID
            partner_id (int, optional): 取引先ID
            account_item_id (int, optional): 勘定科目ID
            partner_code (str, optional): 取引先コード
            status (str, optional): 決済状況 (未決済: unsettled, 完了: settled)
            type (str, optional): 収支区分 (収入: income, 支出: expense)
            start_issue_date (string, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_issue_date (str, optional): 発生日で絞込：終了日(yyyy-mm-dd)
            start_due_date (str, optional): 支払期日で絞込：開始日(yyyy-mm-dd)
            end_due_date (str, optional): 支払期日で絞込：終了日(yyyy-mm-dd)
            start_renew_date (str, optional): +更新日で絞込：開始日(yyyy-mm-dd)
            end_renew_date (str, optional): +更新日で絞込：終了日(yyyy-mm-dd)
            offset (int, optional): 取得レコードのオフセット (デフォルト: 0)
            limit (int, optional): 取得レコードの件数 (デフォルト: 20, 最大: 100)
            registered_from (str, optional): 取引登録元アプリで絞込（me: 本APIを叩くアプリ自身から登録した取引のみ）
            accruals (str, optional): 取引の債権債務行の表示（without: 表示しない(デフォルト), with: 表示する）

        Returns:
            dict: like below
            {
              "deals": [
                {
                  "id": 101,
                  "company_id": 1,
                  "issue_date": "2013-01-01",
                  "due_date": "2013-02-28",
                  "amount": 5250,
                  "due_amount": 0,
                  "type": "expense",
                  "partner_id": 201,
                  "ref_number": "123-456",
                  "status": "settled",
                  "details": [
                    {
                      "id": 11,
                      "account_item_id": 803,
                      "tax_id": 14,
                      "tax_code": 2,
                      "tag_ids": [
                        1,
                        2,
                        3
                      ],
                      "amount": 5250,
                      "vat": 250,
                      "description": "備考",
                      "entry_side": "debit"
                    }
                  ],
                  "renews": [
                    {
                      "id": 11,
                      "update_date": "2014-01-01",
                      "renew_target_id": 12,
                      "renew_target_type": "detail",
                      "details": [
                        {
                          "tax_code": 1,
                          "tag_ids": [
                            1
                          ],
                          "amount": 108000,
                          "account_item_id": 1,
                          "vat": 8000,
                          "id": 1,
                          "entry_side": "debit"
                        }
                      ]
                    }
                  ],
                  "payments": [
                    {
                      "id": 202,
                      "date": "2013-01-28",
                      "from_walletable_type": "bank_account",
                      "from_walletable_id": 103,
                      "amount": 5250
                    }
                  ]
                }
              ],
              "meta": {
                "total_count": 100
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "deals")
        return self.send_request(request_method, url, payload)

    def get_deal(self, deal_id, **payload):

        """取引(収入/支出)の取得

        指定した事業所の取引（収入／支出）を取得する

        Args:
            deal_id (int): 取引ID
            company_id (int): 事務所ID
            accruals(str, optional): 取引の債権債務行の表示（without: 表示しない(デフォルト), with: 表示する）

        Returns:
            dict: like below
            {
              "deal": {
                "id": 101,
                "company_id": 1,
                "issue_date": "2013-01-01",
                "due_date": "2013-02-28",
                "amount": 5250,
                "due_amount": 0,
                "type": "expense",
                "partner_id": 201,
                "ref_number": "123-456",
                "status": "settled",
                "details": [
                  {
                    "id": 11,
                    "account_item_id": 803,
                    "tax_id": 14,
                    "tax_code": 2,
                    "tag_ids": [
                      1,
                      2,
                      3
                    ],
                    "amount": 5250,
                    "vat": 250,
                    "description": "備考",
                    "entry_side": "debit"
                  }
                ],
                "renews": [
                  {
                    "id": 11,
                    "update_date": "2014-01-01",
                    "renew_target_id": 12,
                    "renew_target_type": "detail",
                    "details": [
                      {
                        "tax_code": 1,
                        "tag_ids": [
                          1
                        ],
                        "amount": 108000,
                        "account_item_id": 1,
                        "vat": 8000,
                        "id": 1,
                        "entry_side": "debit"
                      }
                    ]
                  }
                ],
                "payments": [
                  {
                    "id": 202,
                    "date": "2013-01-28",
                    "from_walletable_type": "bank_account",
                    "from_walletable_id": 103,
                    "amount": 5250
                  }
                ]
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["deals", str(deal_id)]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     Expense application line templates(経費科目)
# ===========================================
    def get_expense_application_line_templates(self, **payload):

        """経費科目一覧の取得

        指定した事業所の経費科目一覧を取得する

        Args:
            offset (int): 取得レコードのオフセット (デフォルト: 0)
            limit (int): 取得レコードの件数 (デフォルト: 20, 最大: 100)

        Returns:
            dict: like below
            {
              "expense_application_line_templates": [
                {
                  "id": 1,
                  "name": "交通費",
                  "account_item_name": "旅費交通費",
                  "tax_name": "課対仕入",
                  "description": "電車、バス、飛行機などの交通費",
                  "line_description": "移動区間"
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "expense_application_line_templates")
        return self.send_request(request_method, url, payload)

# ===========================================
#     Journals (仕訳帳)
# ===========================================
    def get_request_downloading_journals(self, **payload):

        """ダウンロード要求

        ユーザが所属する事業所の仕訳帳のダウンロードをリクエストします 生成されるファイルに関しては、ヘルプページをご参照ください

        Args:
            download_type (str): ダウンロード形式. Available values : csv, pdf, yayoi, generic
            company_id (int):  事業所ID
            visible_tags (array[string], optional): 補助科目やコメントとして出力する項目. Available values : partner, item, tag, section, description, wallet_txn_description, all
            start_date (str, optional): 取得開始日 (yyyy-mm-dd)
            end_date (str, optional): 取得終了日 (yyyy-mm-dd)
        Note:
            定義
                download_type
                    csv
                    pdf
                    yayoi (csv alias)
                    generic
                visible_tags : 指定しない場合は従来の仕様の仕訳帳が出力されます
                    partner : 取引先タグ
                    item : 品目タグ
                    tag : メモタグ
                    section : 部門タグ
                    description : 備考欄
                    wallet_txn_description : 明細の備考欄
                    all : 指定された場合は上記の設定をすべて有効として扱います
                id : 受け付けID

        Returns:
            dict: like below
            {
              "journals": {
                "id": 1,
                "messages": ":id でリクエストを受け付けました。",
                "company_id": 1,
                "download_type": "csv",
                "start_date": "2017-05-01",
                "end_date": "2017-05-31",
                "visible_tags": [
                  "all"
                ],
                "status_url": "https://api.freee.co.jp/api/1/journals/reports/4/status"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "journals")
        return self.send_request(request_method, url, payload)

    def get_downloading_journals_status(self, id, **payload):

        """ステータス確認

        ダウンロードリクエストのステータスを確認する
        ＊このAPIは無料プランのアカウントではご利用になれません

        Args:
            company_id (int):  事業所ID
            id (int): 受付ID
            visible_tags (array[string], optional): 補助科目やコメントとして出力する項目. Available values : partner, item, tag, section, description, wallet_txn_description, all
            start_date (str, optional): 取得開始日 (yyyy-mm-dd)
            end_date (str, optional): 取得終了日 (yyyy-mm-dd)
        Note:
            定義
                enqueued : 実行待ち
                working : 実行中
                uploaded : 準備完了
                id : 受け付けID

        Returns:
            dict: like below
            {
              "journals": {
                "id": 1,
                "company_id": 1,
                "download_type": "csv",
                "status": "csv",
                "start_date": "2017-05-01",
                "end_date": "2017-05-31",
                "visible_tags": [
                  "all"
                ],
                "download_url": "https://api.freee.co.jp/api/1/journals/reports/1/download"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["journals", "reports", id, "status"]))
        return self.send_request(request_method, url, payload)

    def get_download_journals(self, id, **payload):

        """ダウンロード実行

        ダウンロードを実行する
        ＊このAPIは無料プランのアカウントではご利用になれません
        ＊レスポンスを直接returnしているので注意

        Args:
            company_id (int):  事業所ID
            id (int): 受付ID
        Note:
            定義
                id : 受け付けID

        Returns:
            None
        """
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["journals", "reports", id, "download"]))

        if self.confirm_expired():
            token_dict = self.run_refresh_token()
            self.save_tokens(token_dict)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }
        res = requests.get(url, headers=headers, params=payload)
        if res.ok:
            return res
        else:
            raise res.raise_for_status()

# ===========================================
#     ManualJournals (振替伝票)
# ===========================================

    def get_manual_journals(self, **payload):

        """振替伝票一覧の取得

        指定した事業所の振替伝票一覧を取得する

        Args:
            company_id (int): 事業所ID
            start_issue_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_issue_date (str, optional): 発生日で絞込：終了日(yyyy-mm-dd)
            entry_side (str, optional): 貸借で絞込 (貸方: credit, 借方: debit). Available values : credit, debit
            account_item_id (int, optional): 勘定科目IDで絞込
            min_amount (int, optional): 金額で絞込：下限
            max_amount (int, optional): 金額で絞込：上限
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択の貸借行を絞り込めます）
            partner_code (str, optional): 取引先コードで絞込
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択の貸借行を絞り込めます）
            section_id (int, optional): 部門IDで絞込（0を指定すると、部門が未選択の貸借行を絞り込めます）
            segment_1_tag_id (int, optional): セグメント１IDで絞り込み（0を指定すると、セグメント１が未選択の貸借行を絞り込めます）
            segment_2_tag_id (int, optional): セグメント２IDで絞り込み（0を指定すると、セグメント２が未選択の貸借行を絞り込めます）
            segment_3_tag_id (int, optional): セグメント３IDで絞り込み（0を指定すると、セグメント３が未選択の貸借行を絞り込めます）
            comment_status (str, optional): コメント状態で絞込（自分宛のコメント: posted_with_mention, 自分宛のコメント-未解決: raised_with_mention, 自分宛のコメント-解決済: resolved_with_mention, コメントあり: posted, 未解決: raised, 解決済: resolved, コメントなし: none）Available values : posted_with_mention, raised_with_mention, resolved_with_mention, posted, raised, resolved, none
            comment_important (bool, optional): 重要コメント付きの振替伝票を絞込
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）.Available values : only, without
            txn_number (str, optional): 仕訳番号で絞込（事業所の仕訳番号形式が有効な場合のみ）
            offset  (int, optional): 取得レコードのオフセット (デフォルト: 0)
            limit (int, optional): 取得レコードの件数 (デフォルト: 20, 最大: 500)
        Note:
            定義
                issue_date : 発生日
                adjustment : 決算整理仕訳フラグ（true: 決算整理仕訳, false: 日常仕訳）
                txn_number : 仕訳番号
                details : 振替伝票の貸借行
                entry_side : 貸借区分
                    credit : 貸方
                    debit : 借方
                amount : 金額

            注意点
                振替伝票は売掛・買掛レポートには反映されません。債権・債務データの登録は取引(Deals)をお使いください。
                事業所の仕訳番号形式が有効な場合のみ、レスポンスで仕訳番号(txn_number)を返します。
                セグメントタグ情報は法人向けのプロフェッショナルプラン以上で利用可能です。利用可能なセグメントの数は、法人向けのプロフェッショナルプランの場合は1つ、エンタープライズプランの場合は3つです。
                partner_codeを利用するには、事業所の設定から取引先コードの利用を有効にする必要があります。またpartner_codeとpartner_idは同時に指定することはできません。

        Returns:
            dict: like below
            {
              "manual_journals": [
                {
                  "id": 1,
                  "company_id": 1,
                  "issue_date": "2018-01-01",
                  "adjustment": false,
                  "details": [
                    {
                      "id": 1,
                      "entry_side": "credit",
                      "account_item_id": 1,
                      "tax_code": 1,
                      "tag_ids": [
                        1
                      ],
                      "tag_names": [
                        "メモタグ"
                      ],
                      "segment_1_tag_id": 1,
                      "segment_1_tag_name": 0,
                      "segment_2_tag_id": 1,
                      "segment_2_tag_name": 0,
                      "segment_3_tag_id": 1,
                      "segment_3_tag_name": 0,
                      "amount": 108000,
                      "vat": 8000,
                      "description": "備考"
                    }
                  ]
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, "manual_journals")
        return self.send_request(request_method, url, payload)

    def get_manual_journal(self, id, **payload):

        """振替伝票の取得

        指定した事業所の振替伝票を取得する

        Args:
            company_id (int): 事業所ID
            id (int): 振替伝票ID
        Note:
            定義
                issue_date : 発生日
                adjustment : 決算整理仕訳フラグ（true: 決算整理仕訳, false: 日常仕訳）
                txn_number : 仕訳番号
                details : 振替伝票の貸借行
                entry_side : 貸借区分
                    credit : 貸方
                    debit : 借方
                amount : 金額

            注意点
                振替伝票は売掛・買掛レポートには反映されません。債権・債務データの登録は取引(Deals)をお使いください。
                事業所の仕訳番号形式が有効な場合のみ、レスポンスで仕訳番号(txn_number)を返します。
                セグメントタグ情報は法人向けのプロフェッショナルプラン以上で利用可能です。利用可能なセグメントの数は、法人向けのプロフェッショナルプランの場合は1つ、エンタープライズプランの場合は3つです。

        Returns:
            dict: like below
            {
              "manual_journal": {
                "id": 1,
                "company_id": 1,
                "issue_date": "2018-01-01",
                "adjustment": false,
                "details": [
                  {
                    "id": 1,
                    "entry_side": "credit",
                    "account_item_id": 1,
                    "tax_code": 1,
                    "tag_ids": [
                      1
                    ],
                    "tag_names": [
                      "メモタグ"
                    ],
                    "segment_1_tag_id": 1,
                    "segment_1_tag_name": 0,
                    "segment_2_tag_id": 1,
                    "segment_2_tag_name": 0,
                    "segment_3_tag_id": 1,
                    "segment_3_tag_name": 0,
                    "amount": 108000,
                    "vat": 8000,
                    "description": "備考"
                  }
                ]
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["manual_journals", id]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     Trial balance (試算表)
# ===========================================

    def get_reports_trial_bs(self, **payload):
        """貸借対照表の取得

        指定した事業所の貸借対照表を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                opening_balance : 期首残高
                debit_amount : 借方金額
                credit_amount: 貸方金額
                closing_balance : 期末残高
                composition_ratio : 構成比

            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_bs": {
                "company_id": 1,
                "fiscal_year": 2019,
                "start_month": 1,
                "end_month": 12,
                "start_date": "2019-01-01",
                "end_date": "2019-12-31",
                "account_item_display_type": "account_item",
                "breakdown_display_type": "partner",
                "partner_id": 1,
                "partner_code": "code001",
                "item_id": 1,
                "adjustment": "only",
                "created_at": "2018-09-10T13:47:24.000+09:00",
                "balances": [
                  {
                    "account_item_id": 192,
                    "account_item_name": "現金",
                    "partners": [
                      {
                        "id": 22,
                        "name": "freee",
                        "opening_balance": 0,
                        "debit_amount": 0,
                        "credit_amount": 2592,
                        "closing_balance": -25920,
                        "composition_ratio": 0.85
                      }
                    ],
                    "items": [
                      {
                        "id": 1,
                        "name": "源泉所得税",
                        "opening_balance": 0,
                        "debit_amount": 0,
                        "credit_amount": 2592,
                        "closing_balance": -25920,
                        "composition_ratio": 0.85
                      }
                    ],
                    "account_category_id": 8,
                    "account_category_name": "流動資産",
                    "total_line": true,
                    "hierarchy_level": 3,
                    "parent_account_category_id": 19,
                    "parent_account_category_name": "他流動資産",
                    "opening_balance": 0,
                    "debit_amount": 0,
                    "credit_amount": 2592,
                    "closing_balance": -25920,
                    "composition_ratio": 0.85
                  }
                ]
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_bs"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_bs_two_years(self, **payload):
        """貸借対照表(前年比較)の取得

        指定した事業所の貸借対照表(前年比較)を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                last_year_closing_balance: 前年度期末残高
                closing_balance : 期末残高

            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_bs_two_years" :
                {
                  "company_id" : 1,
                  "fiscal_year" : 2017,
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1000,
                    "account_item_name" : "現金",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "流動資産",
                    "last_year_closing_balance" : 25000,
                    "closing_balance" : 100000,
                    "year_on_year" : 0.85
                      },
                      ...
                      ]
                }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_bs_two_years"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_bs_three_years(self, **payload):
        """貸借対照表(３期間比較)の取得

        指定した事業所の貸借対照表(３期間比較)を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without

        Note:
            定義

                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                closing_balance : 期末残高
                two_years_before_closing_balance: 前々年度期末残高
                last_year_closing_balance: 前年度期末残高
                year_on_year : 前年比

            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_bs_three_years" :
                {
                  "company_id" : 1,
                  "fiscal_year" : 2017,
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1000,
                    "account_item_name" : "現金",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "流動資産",
                    "two_year_before_closing_balance" : 50000,
                    "last_year_closing_balance" : 25000,
                    "closing_balance" : 100000,
                    "year_on_year" : 0.85
                  },
                  ...
                  ]
                }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_bs_three_years"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_pl(self, **payload):
        """損益計算書の取得

        指定した事業所の損益計算書(前年比較)を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            section_id (int, optional): 部門IDで絞込（0を指定すると、部門が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without
            cost_allocation (str, optional): 配賦仕訳で絞込（配賦仕訳のみ：only,配賦仕訳以外：without）Available values : only, not_include

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                opening_balance : 期首残高
                debit_amount : 借方金額
                credit_amount: 貸方金額
                closing_balance : 期末残高
                composition_ratio : 構成比


            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_pl" :
                {
                  "company_id" : 1,
                  "fiscal_year" : 2017,
                  "breakdown_display_type" : "partner",
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1500,
                    "account_item_name" : "売上高",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "営業収益",
                    "opening_balance" : 100000,
                    "debit_amount" : 50000,
                    "credit_amount" : 20000,
                    "closing_balance" : 130000,
                    "composition_ratio" : 0.25
                    "partners" : [{
                      "id" : 123,
                      "name" : "freee",
                      "long_name" : "freee株式会社",
                      "opening_balance" : 100000,
                      "debit_amount" : 50000,
                      "credit_amount" : 20000,
                      "closing_balance" : 130000,
                      "composition_ratio" : 0.25
                      },
                    ...
                    ]
                  },
                  ...
                  ]
                }
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_pl"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_pl_two_years(self, **payload):
        """損益計算書(前年比較)の取得

        指定した事業所の損益計算書(前年比較)を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            section_id (int, optional): 部門IDで絞込（0を指定すると、部門が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without
            cost_allocation (str, optional): 配賦仕訳で絞込（配賦仕訳のみ：only,配賦仕訳以外：without）Available values : only, not_include

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                last_year_closing_balance: 前年度期末残高
                closing_balance : 期末残高
                year_on_year : 前年比

            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_pl_two_years" :
                {
                  "company_id" : 1,
                  "fiscal_year" : 2017,
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1500,
                    "account_item_name" : "売上高",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "営業収益",
                    "last_year_closing_balance" : 25000,
                    "closing_balance" : 100000,
                    "year_on_year" : 0.85
                  },
                  ...
                  ]
                }
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_pl_two_years"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_pl_three_years(self, **payload):
        """損益計算書(前年比較)の取得

        指定した事業所の損益計算書(３期間比較)を取得する

        Args:
            company_id (int): 事業所ID
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            section_id (int, optional): 部門IDで絞込（0を指定すると、部門が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without
            cost_allocation (str, optional): 配賦仕訳で絞込（配賦仕訳のみ：only,配賦仕訳以外：without）Available values : only, not_include

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                two_years_before_closing_balance: 前々年度期末残高
                last_year_closing_balance: 前年度期末残高
                closing_balance : 期末残高
                year_on_year : 前年比

            注意点
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_pl_three_years" :
                {
                  "company_id" : 1,
                  "fiscal_year" : 2017,
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1500,
                    "account_item_name" : "売上高",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "営業収益",
                    "two_year_before_closing_balance" : 50000,
                    "last_year_closing_balance" : 25000,
                    "closing_balance" : 100000,
                    "year_on_year" : 0.85
                  },
                  ...
                  ]
                }
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_pl_three_years"]))
        return self.send_request(request_method, url, payload)

    def get_reports_trial_pl_sections(self, **payload):
        """損益計算書(部門比較)の取得

        指定した事業所の損益計算書(部門比較)を取得する

        Args:
            company_id (int): 事業所ID
            section_ids (str): 出力する部門の指定（半角数字のidを半角カンマ区切りスペースなしで指定してください）
            fiscal_year (int, optional): 会計年度
            start_month (int, optional): 発生月で絞込：開始会計月(mm)
            end_month (int, optional): 発生月で絞込：終了会計月(mm)
            start_date (str, optional): 発生日で絞込：開始日(yyyy-mm-dd)
            end_date (str, optional) 発生日で絞込：終了日(yyyy-mm-dd)
            account_item_display_type (str, optional): 勘定科目の表示（勘定科目: account_item, 決算書表示:group）. Available values : account_item, group
            breakdown_display_type (str, optional): 内訳の表示（取引先: partner, 品目: item, 勘定科目: account_item） ※勘定科目はaccount_item_display_typeが「group」の時のみ指定できます. Available values : partner, item, account_item
            partner_id (int, optional): 取引先IDで絞込（0を指定すると、取引先が未選択で絞り込めます）
            partner_code (str, optional): 取引先コードで絞込（事業所設定で取引先コードの利用を有効にしている場合のみ利用可能です）
            item_id (int, optional): 品目IDで絞込（0を指定すると、品目が未選択で絞り込めます）
            section_id (int, optional): 部門IDで絞込（0を指定すると、部門が未選択で絞り込めます）
            adjustment (str, optional): 決算整理仕訳で絞込（決算整理仕訳のみ: only, 決算整理仕訳以外: without）. Available values : only, without
            cost_allocation (str, optional): 配賦仕訳で絞込（配賦仕訳のみ：only,配賦仕訳以外：without）Available values : only, not_include

        Note:
            定義
                created_at : 作成日時
                account_item_name : 勘定科目名
                hierarchy_level: 階層レベル
                parent_account_item_name: 親の勘定科目名
                closing_balance : 期末残高

            注意点
                個人向けのプレミアムプラン、法人向けのビジネスプラン以上で利用可能なAPIです。対象外のプランでは401エラーを返却します。
                会計年度が指定されない場合、現在の会計年度がデフォルトとなります。
                絞り込み条件の日付と、月または年度は同時に指定することはできません。

        Returns:
            dict: like below
            {
              "trial_pl_sections" :
                {
                  "company_id" : 1,
                  "section_ids" : "1,2,3",
                  "fiscal_year" : 2017,
                  "created_at" : "2018-05-01 12:00:50"
                  "balances" : [{
                    "account_item_id" : 1500,
                    "account_item_name" : "売上高",
                    "hierarchy_level" : 2,
                    "parent_account_item_id" : 100;
                    "parent_account_item_name" : "営業収益",
                    "closing_balance" : 1000000,
                    "sections" : [{
                      "id": 1
                      "name": "営業部",
                      "closing_balance" : 100000
                    },
                    {
                      "id": 2
                      "name": "広報部",
                      "closing_balance" : 200000
                    },
                    {
                      "id": 3
                      "name": "人事部",
                      "closing_balance" : 300000
                    },
                    ...
                    ]
                  },
                  ...
                  ]
                }
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["reports", "trial_pl_sections"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     Walletables (口座)
# ===========================================

    def get_walletables(self, **payload):
        """口座一覧の取得

        指定した事業所の口座一覧を取得する

        Args:
            company_id (int): 事業所ID
            with_balance (boool): 残高情報を含める

        Note:
            定義
                type
                    bank_account : 銀行口座
                    credit_card : クレジットカード
                    wallet : その他の決済口座
                walletable_balance : 登録残高
                last_balance : 同期残高

        Returns:
            dict: like below
            {
              "walletables": [
                {
                  "id": 1,
                  "name": "freee銀行",
                  "bank_id": 3,
                  "type": "bank_account",
                  "last_balance": 1565583,
                  "walletable_balance": 1340261
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.account_endpoint, ("/").join(["walletables"]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     人事労務freee API
# ===========================================

# ===========================================
#     タイムレコーダー（打刻）（タイムレコーダー（打刻）機能の操作）
# ===========================================
    def get_time_clocks(self, employee_id, **payload):

        """打刻情報の一覧取得

        指定した従業員・期間の打刻情報を返します。
        デフォルトでは従業員の当月の打刻開始日から当日までの値が返ります。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            from_date(int, optional): 取得する打刻期間の開始日(YYYY-MM-DD)(例:2018-08-01)(デフォルト: 当月の打刻開始日)
            to_date(int, optional): 取得する打刻期間の終了日(YYYY-MM-DD)(例:2018-08-31)(デフォルト: 当日)
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            {
              "employee_time_clocks": [
                {
                  "id": 0,
                  "date": "string",
                  "type": "string",
                  "datetime": "2019-10-14T05:23:47.261Z",
                  "original_datetime": "2019-10-14T05:23:47.261Z",
                  "note": "string"
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "time_clocks"]))
        return self.send_request(request_method, url, payload)

    def get_time_clock(self, employee_id, time_clock_id, **payload):

        """打刻情報の詳細取得

        指定した従業員・指定した打刻の詳細情報を返します。
        打刻情報の一覧取得APIにて取得した打刻IDを利用することができます。

        Args:
            employee_id (str): 従業員ID
            time_clock_id (str): 打刻情報ID
            company_id (int): 事務所ID

        Returns:
            dict: like below
            {
              "employee_time_clock": {
                "id": 0,
                "date": "string",
                "type": "string",
                "datetime": "2019-10-14T05:28:58.011Z",
                "original_datetime": "2019-10-14T05:28:58.011Z",
                "note": "string"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "time_clocks", time_clock_id]))
        return self.send_request(request_method, url, payload)

    def get_time_clock_available_types(self, employee_id, **payload):

        """打刻可能種別の取得

        指定した従業員・日付の打刻可能種別と打刻基準日を返します。
        例: すでに出勤した状態だと、休憩開始、退勤が配列で返ります。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            date (date, optional): 対象日(YYYY-MM-DD)(例:2018-08-01)(デフォルト：当日)

        Returns:
            dict: like below
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "time_clocks/available_types"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     ログインユーザー（ログインユーザーの取得）
# ===========================================
    def get_login_user(self, **payload):

        """ログインユーザーの取得

        このリクエストの認可セッションにおけるログインユーザの情報を返します。人事労務freeeでは一人のログインユーザを複数の事業所に関連付けられるため、このユーザと関連のあるすべての事業所の情報をリストで返します。他のAPIのパラメータとして company_id が求められる場合は、このAPIで取得した company_id を使用します。

        Args:
            No parameters

        Returns:
            dict: like below
            {
              "id": 0,
              "companies": [
                {
                  "id": 0,
                  "name": "string",
                  "role": "string",
                  "external_cid": "string",
                  "employee_id": 0,
                  "display_name": "string"
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, "users/me")
        return self.send_request(request_method, url, payload)

# ===========================================
#     給与明細（給与明細の操作)
# ===========================================
    def get_salaries_employee_payroll_statements(self, **payload):

        """給与明細情報を取得

        指定した事業所に所属する従業員の給与明細をリストで返します。
        指定した年月に支払いのある給与明細が返されます。

        Args:
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
                {
                  "employee_payroll_statements": [
                    {
                      "id": 0,
                      "company_id": 0,
                      "employee_id": 0,
                      "employee_name": "string",
                      "employee_display_name": "string",
                      "employee_num": "string",
                      "pay_date": "string",
                      "start_date": "string",
                      "closing_date": "string",
                      "variable_pay_start_date": "string",
                      "variable_pay_closing_date": "string",
                      "fixed": true,
                      "calc_status": "string",
                      "calculated_at": "2019-10-12T14:15:27.217Z",
                      "pay_calc_type": "string",
                      "basic_pay_amount": "string",
                      "work_days": "string",
                      "normal_work_time": "string",
                      "normal_work_days": "string",
                      "work_mins_by_paid_holiday": "string",
                      "num_paid_holidays": "string",
                      "is_board_member": true,
                      "total_attendance_deduction_amount": "string",
                      "total_allowance_amount": "string",
                      "total_deduction_amount": "string",
                      "net_payment_amount": "string",
                      "gross_payment_amount": "string",
                      "total_worked_days_count": "string",
                      "total_taxable_payment_amount": "string",
                      "total_expense_amount": "string",
                      "total_transfer_amount": "string",
                      "total_annual_payment_amount": "string",
                      "payments": [
                        {
                          "name": "string",
                          "amount": "string"
                        }
                      ],
                      "deductions": [
                        {
                          "name": "string",
                          "amount": "string"
                        }
                      ],
                      "attendances": [
                        {
                          "name": "string",
                          "time": "string",
                          "amount": "string"
                        }
                      ],
                      "overtime_pays": [
                        {
                          "name": "string",
                          "time": "string",
                          "amount": "string"
                        }
                      ],
                      "remark": "string"
                    }
                  ]
                }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, "salaries/employee_payroll_statements")
        return self.send_request(request_method, url, payload)

    def get_salaries_employee_payroll_statement(self, employee_id, **payload):

        """特定の従業員の給与明細情報を取得

        指定した従業員ID、年月の給与明細を返します。
        指定した年月に支払いのある給与明細が返されます。


        Args:
            employee_id (str): 従業員ID
            company_id (int): 事務所ID
            year (int): 対象年
            month (int): 対象月
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            {
              "employee_payroll_statement": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "employee_name": "string",
                "employee_display_name": "string",
                "employee_num": "string",
                "pay_date": "string",
                "start_date": "string",
                "closing_date": "string",
                "variable_pay_start_date": "string",
                "variable_pay_closing_date": "string",
                "fixed": true,
                "calc_status": "string",
                "calculated_at": "2019-10-12T14:21:53.194Z",
                "pay_calc_type": "string",
                "basic_pay_amount": "string",
                "work_days": "string",
                "normal_work_time": "string",
                "normal_work_days": "string",
                "work_mins_by_paid_holiday": "string",
                "num_paid_holidays": "string",
                "is_board_member": true,
                "total_attendance_deduction_amount": "string",
                "total_allowance_amount": "string",
                "total_deduction_amount": "string",
                "net_payment_amount": "string",
                "gross_payment_amount": "string",
                "total_worked_days_count": "string",
                "total_taxable_payment_amount": "string",
                "total_expense_amount": "string",
                "total_transfer_amount": "string",
                "total_annual_payment_amount": "string",
                "payments": [
                  {
                    "name": "string",
                    "amount": "string"
                  }
                ],
                "deductions": [
                  {
                    "name": "string",
                    "amount": "string"
                  }
                ],
                "attendances": [
                  {
                    "name": "string",
                    "time": "string",
                    "amount": "string"
                  }
                ],
                "overtime_pays": [
                  {
                    "name": "string",
                    "time": "string",
                    "amount": "string"
                  }
                ],
                "remark": "string"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["salaries/employee_payroll_statements", str(employee_id)]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     勤怠（勤怠の操作)
# ===========================================

    def delete_work_record(self, employee_id, date, payload):

        """勤怠情報削除

        指定した従業員の勤怠情報を削除します。

        Args:
            employee_id (str): 従業員ID
            date (str): 指定日 like 2019-09-01
            payload (dict): Request params

        Request params:
            {
              "company_id": 0
            }

        Returns:
        """
        request_method = "delete"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", str(employee_id), "work_records", date]))
        return self.send_request(request_method, url, payload)

    def get_work_record(self, employee_id, date, **payload):

        """勤怠情報取得

        指定した従業員・日付の勤怠情報を返します。

        Args:
            employee_id (str): 従業員ID
            date (str): 指定日 like 2019-09-01
            company_id (int): 事務所ID

        Returns:
            dict: like below
            {
              "break_records": [
                {
                  "clock_in_at": "2019-10-12T15:19:35.625Z",
                  "clock_out_at": "2019-10-12T15:19:35.625Z"
                }
              ],
              "clock_in_at": "2019-10-12T15:19:35.625Z",
              "clock_out_at": "2019-10-12T15:19:35.625Z",
              "date": "2019-10-12T15:19:35.625Z",
              "day_pattern": "string",
              "schedule_pattern": "string",
              "early_leaving_mins": 0,
              "is_absence": false,
              "is_editable": true,
              "lateness_mins": 0,
              "normal_work_clock_in_at": "2019-10-12T15:19:35.625Z",
              "normal_work_clock_out_at": "2019-10-12T15:19:35.625Z",
              "normal_work_mins": 0,
              "normal_work_mins_by_paid_holiday": 0,
              "note": "string",
              "paid_holiday": 0.5,
              "use_attendance_deduction": true,
              "use_default_work_pattern": true,
              "total_overtime_work_mins": 0,
              "total_holiday_work_mins": 0,
              "total_latenight_work_mins": 0
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", str(employee_id), "work_records", date]))
        return self.send_request(request_method, url, payload)

    def put_work_record(self, employee_id, date, payload):
        """勤怠情報更新

        指定した従業員の勤怠情報を更新します。

        Args:
            employee_id (str): 従業員ID
            date (str): 指定日 like 2019-09-01
            payload (dict): Request params

        Request params:
            出勤日について出退勤時刻および休憩時間を更新する場合は以下のようなパラメータをリクエストします。
                {
                  "work_record": {
                    "company_id": 1,
                    "break_records": [
                      {
                        "clock_in_at": "2017-05-25T12:00:00.000+09:00",
                        "clock_out_at": "2017-05-25T13:00:00.000+09:00"
                      }
                    ],
                    "clock_in_at": "2017-05-25T09:10:00.000+09:00",
                    "clock_out_at": "2017-05-25T18:20:00.000+09:00"
                  }
                }

            勤務パターンや既定の所定労働時間を変更する場合は use_default_work_pattern に false を指定するとともに、各設定を上書きするパラメータをリクエストします。
                {
                  "work_record": {
                    "company_id": 1,
                    "break_records": [
                      {
                        "clock_in_at": "2017-05-25T12:00:00.000+09:00",
                        "clock_out_at": "2017-05-25T13:00:00.000+09:00"
                      }
                    ],
                    "clock_in_at": "2017-05-25T09:10:00.000+09:00",
                    "clock_out_at": "2017-05-25T18:20:00.000+09:00",
                    "day_pattern": "normal_day",
                    "normal_work_clock_in_at": "2017-05-25T01100:00.000+09:00",
                    "normal_work_clock_out_at": "2017-12-20T20:00:00.000+09:00",
                    "normal_work_mins": 0,
                    "use_default_work_pattern": false
                  }
                }

            欠勤を付ける場合は company_idとis_absence 以外のパラメータは必要ありません。
                {
                  "work_record": {
                    "company_id": 1,
                    "is_absence": true
                  }
                }

        Returns:
            dict: like below
                {
                  "break_records": [
                    {
                      "clock_in_at": "2019-10-27T12:52:52.524Z",
                      "clock_out_at": "2019-10-27T12:52:52.524Z"
                    }
                  ],
                  "clock_in_at": "2019-10-27T12:52:52.524Z",
                  "clock_out_at": "2019-10-27T12:52:52.524Z",
                  "date": "2019-10-27T12:52:52.524Z",
                  "day_pattern": "string",
                  "schedule_pattern": "string",
                  "early_leaving_mins": 0,
                  "is_absence": false,
                  "is_editable": true,
                  "lateness_mins": 0,
                  "normal_work_clock_in_at": "2019-10-27T12:52:52.524Z",
                  "normal_work_clock_out_at": "2019-10-27T12:52:52.524Z",
                  "normal_work_mins": 0,
                  "normal_work_mins_by_paid_holiday": 0,
                  "note": "string",
                  "paid_holiday": 0.5,
                  "use_attendance_deduction": true,
                  "use_default_work_pattern": true,
                  "total_overtime_work_mins": 0,
                  "total_holiday_work_mins": 0,
                  "total_latenight_work_mins": 0
                }
        """
        request_method = "put"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", str(employee_id), "work_records", date]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     勤怠情報サマリ（勤怠情報の月次サマリの操作)
# ===========================================

    def get_work_record_summaries(self, employee_id, year, month, **payload):

        """勤怠情報月次サマリの取得

        指定した従業員、月の勤怠情報のサマリを返します。work_recordsオプションにtrueを指定することで、明細となる日次の勤怠情報もあわせて返却します。

        Args:
            employee_id (str): 従業員ID
            year (int): 指定年
            month (int): 指定月
            company_id (int): 事務所ID
            work_records (str, optional): サマリ情報に日次の勤怠情報を含める(true/false)(デフォルト: false)

        Returns:
            dict: like below
            {
              "year": 0,
              "month": 0,
              "start_date": "string",
              "end_date": "string",
              "work_days": 0,
              "total_work_mins": 0,
              "total_normal_work_mins": 0,
              "total_excess_statutory_work_mins": 0,
              "total_overtime_except_normal_work_mins": 0,
              "total_overtime_within_normal_work_mins": 0,
              "total_holiday_work_mins": 0,
              "total_latenight_work_mins": 0,
              "num_absences": 0,
              "num_paid_holidays": 0,
              "num_paid_holidays_left": 0,
              "num_substitute_holidays_used": 0,
              "num_compensatory_holidays_used": 0,
              "num_special_holidays_used": 0,
              "total_lateness_and_early_leaving_mins": 0,
              "work_records": [
                {
                  "break_records": [
                    {
                      "clock_in_at": "2019-10-12T15:06:06.666Z",
                      "clock_out_at": "2019-10-12T15:06:06.666Z"
                    }
                  ],
                  "clock_in_at": "2019-10-12T15:06:06.666Z",
                  "clock_out_at": "2019-10-12T15:06:06.666Z",
                  "date": "2019-10-12T15:06:06.666Z",
                  "day_pattern": "string",
                  "schedule_pattern": "string",
                  "early_leaving_mins": 0,
                  "is_absence": false,
                  "is_editable": true,
                  "lateness_mins": 0,
                  "normal_work_clock_in_at": "2019-10-12T15:06:06.666Z",
                  "normal_work_clock_out_at": "2019-10-12T15:06:06.666Z",
                  "normal_work_mins": 0,
                  "normal_work_mins_by_paid_holiday": 0,
                  "note": "string",
                  "paid_holiday": 0.5,
                  "use_attendance_deduction": true,
                  "use_default_work_pattern": true,
                  "total_overtime_work_mins": 0,
                  "total_holiday_work_mins": 0,
                  "total_latenight_work_mins": 0
                }
              ]
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", str(employee_id), "work_record_summaries", str(year), str(month)]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     従業員情報（従業員の操作)
# ===========================================

    def get_all_employees(self, company_id, **payload):

        """従業員情報を取得

        指定した事業所に所属する退職者も含めた従業員をリストで返します。

        Args:
            company_id (int): 事務所ID
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            [{
                "id": 0,
                "num": "string",
                "display_name": "string",
                "entry_date": "2019-10-12T14:05:59.702Z",
                "retire_date": "2019-10-12T14:05:59.702Z",
                "user_id": 0,
                "email": "string"
              }]
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["companies", str(company_id), "employees"]))
        return self.send_request(request_method, url, payload)

    def get_employees_at_designated_date(self, **payload):
        """従業員情報を取得

        指定した事業所、指定年月に所属する従業員をリストで返します。

        Args:
            company_id (int): 事務所ID
            year (int): 対象年
            month (int): 対象月
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            {
              "employees": [
                {
                  "id": 0,
                  "company_id": 0,
                  "num": "string",
                  "display_name": "string",
                  "base_pension_num": "string",
                  "employment_insurance_reference_number": "string",
                  "birth_date": "string",
                  "entry_date": "string",
                  "retire_date": "string",
                  "user_id": 0,
                  "profile_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "last_name": "string",
                    "first_name": "string",
                    "last_name_kana": "string",
                    "first_name_kana": "string",
                    "zipcode1": "string",
                    "zipcode2": "string",
                    "pref": "string",
                    "address": "string",
                    "address_kana": "string",
                    "phone1": "string",
                    "phone2": "string",
                    "phone3": "string",
                    "residential_zipcode1": "string",
                    "residential_zipcode2": "string",
                    "residential_pref": "string",
                    "residential_address": "string",
                    "residential_address_kana": "string",
                    "employment_type": "string",
                    "title": "string",
                    "gender": 0,
                    "married": true,
                    "is_working_student": true,
                    "widow_type": "string",
                    "disability_type": "string"
                  },
                  "health_insurance_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "entried": true,
                    "reference_num": "string",
                    "standard_monthly_remuneration": 0
                  },
                  "welfare_pension_insurance_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "entried": true,
                    "reference_num": "string",
                    "standard_monthly_remuneration": 0
                  },
                  "dependent_rules": [
                    {
                      "id": 0,
                      "company_id": 0,
                      "employee_id": 0,
                      "last_name": "string",
                      "first_name": "string",
                      "last_name_kana": "string",
                      "first_name_kana": "string",
                      "gender": 0,
                      "relationship": "string",
                      "birth_date": "string",
                      "residence_type": "string",
                      "zipcode1": "string",
                      "zipcode2": "string",
                      "pref": "string",
                      "address": "string",
                      "address_kana": "string",
                      "base_pension_num": "string",
                      "income": 0,
                      "annual_revenue": 0,
                      "disability_type": "string",
                      "occupation": "string",
                      "annual_remittance_amount": 0,
                      "social_insurance_and_tax_dependent": "string"
                    }
                  ],
                  "bank_account_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "bank_name": "string",
                    "bank_name_kana": "string",
                    "bank_code": "string",
                    "branch_name": "string",
                    "branch_name_kana": "string",
                    "branch_code": "string",
                    "account_number": "string",
                    "account_name": "string",
                    "account_type": "string"
                  },
                  "basic_pay_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "pay_calc_type": "string",
                    "pay_amount": 0
                  }
                }
              ],
              "total_count": 0
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, "employees")
        return self.send_request(request_method, url, payload)

    def get_employee(self, employee_id, **payload):
        """特定の従業員情報を取得

        指定したIDの従業員を返します。

        Args:
            id: 従業員ID
            company_id (int): 事務所ID
            year (int): 対象年
            month (int): 対象月

        Returns:
            dict: like below
            {
              "employee": {
                "id": 0,
                "company_id": 0,
                "num": "string",
                "display_name": "string",
                "base_pension_num": "string",
                "employment_insurance_reference_number": "string",
                "birth_date": "string",
                "entry_date": "string",
                "retire_date": "string",
                "user_id": 0,
                "profile_rule": {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "last_name": "string",
                  "first_name": "string",
                  "last_name_kana": "string",
                  "first_name_kana": "string",
                  "zipcode1": "string",
                  "zipcode2": "string",
                  "pref": "string",
                  "address": "string",
                  "address_kana": "string",
                  "phone1": "string",
                  "phone2": "string",
                  "phone3": "string",
                  "residential_zipcode1": "string",
                  "residential_zipcode2": "string",
                  "residential_pref": "string",
                  "residential_address": "string",
                  "residential_address_kana": "string",
                  "employment_type": "string",
                  "title": "string",
                  "gender": 0,
                  "married": true,
                  "is_working_student": true,
                  "widow_type": "string",
                  "disability_type": "string"
                },
                "health_insurance_rule": {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "entried": true,
                  "reference_num": "string",
                  "standard_monthly_remuneration": 0
                },
                "welfare_pension_insurance_rule": {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "entried": true,
                  "reference_num": "string",
                  "standard_monthly_remuneration": 0
                },
                "dependent_rules": [
                  {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "last_name": "string",
                    "first_name": "string",
                    "last_name_kana": "string",
                    "first_name_kana": "string",
                    "gender": 0,
                    "relationship": "string",
                    "birth_date": "string",
                    "residence_type": "string",
                    "zipcode1": "string",
                    "zipcode2": "string",
                    "pref": "string",
                    "address": "string",
                    "address_kana": "string",
                    "base_pension_num": "string",
                    "income": 0,
                    "annual_revenue": 0,
                    "disability_type": "string",
                    "occupation": "string",
                    "annual_remittance_amount": 0,
                    "social_insurance_and_tax_dependent": "string"
                  }
                ],
                "bank_account_rule": {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "bank_name": "string",
                  "bank_name_kana": "string",
                  "bank_code": "string",
                  "branch_name": "string",
                  "branch_name_kana": "string",
                  "branch_code": "string",
                  "account_number": "string",
                  "account_name": "string",
                  "account_type": "string"
                },
                "basic_pay_rule": {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "pay_calc_type": "string",
                  "pay_amount": 0
                }
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", str(employee_id)]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     従業員の基本給(従業員の基本給の操作)
# ===========================================

    def get_basic_pay_rule(self, employee_id, **payload):

        """従業員の基本給の取得

        指定した従業員・日付の基本給情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
            {
              "employee_basic_pay_rule": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "pay_calc_type": "string",
                "pay_amount": 0
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "basic_pay_rule"]))
        return self.send_request(request_method, url, payload)

# ===========================================
#     従取得業員の銀行口座(従業員の銀行口座の操作)
# ===========================================

    def get_bank_account_rule(self, employee_id, **payload):

        """銀行口座の取得

        指定した従業員・日付の銀行口座情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
            {
              "employee_bank_account_rule": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "bank_name": "string",
                "bank_name_kana": "string",
                "bank_code": "string",
                "branch_name": "string",
                "branch_name_kana": "string",
                "branch_code": "string",
                "account_number": "string",
                "account_name": "string",
                "account_type": "string"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "bank_account_rule"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     従業員の健康保険(従業員の健康保険の操作)
# ===========================================
    def get_health_insurance_rule(self, employee_id, **payload):

        """健康保険情報を返します。

        指定した従業員・日付の健康保険情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
            {
              "employee_health_insurance_rule": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "entried": true,
                "reference_num": "string",
                "standard_monthly_remuneration": 0
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "health_insurance_rule"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     従業員の厚生年金保険(従業員の厚生年金保険の操作)
# ===========================================
    def get_welfare_pension_insurance_rule(self, employee_id, **payload):

        """厚生年金保険情報を返します。

        指定した従業員・日付の厚生年金保険情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
            {
              "employee_welfare_pension_insurance_rule": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "entried": true,
                "reference_num": "string",
                "standard_monthly_remuneration": 0
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "welfare_pension_insurance_rule"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     従業員の姓名・住所など(従業員の姓名・住所などの操作)
# ===========================================
    def get_profile_rule(self, employee_id, **payload):

        """従業員の姓名などの情報を返します。

        指定した従業員・日付の姓名などの情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            {
              "employee_profile_rule": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "last_name": "string",
                "first_name": "string",
                "last_name_kana": "string",
                "first_name_kana": "string",
                "zipcode1": "string",
                "zipcode2": "string",
                "pref": "string",
                "address": "string",
                "address_kana": "string",
                "phone1": "string",
                "phone2": "string",
                "phone3": "string",
                "residential_zipcode1": "string",
                "residential_zipcode2": "string",
                "residential_pref": "string",
                "residential_address": "string",
                "residential_address_kana": "string",
                "employment_type": "string",
                "title": "string",
                "gender": 0,
                "married": true,
                "is_working_student": true,
                "widow_type": "string",
                "disability_type": "string"
              }
            }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "profile_rule"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     従業員の扶養親族(従業員の扶養親族の操作)
# ===========================================
    def get_dependent_rules(self, employee_id, **payload):

        """従業員の扶養親族情報を返します。

        指定した従業員・日付の扶養親族情報を返します。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["employees", employee_id, "dependent_rules"]))
        return self.send_request(request_method, url, payload)


# ===========================================
#     所属(所属の操作)
# ===========================================

    def get_employee_group_memberships(self, **payload):

        """所属一覽の取得

        指定した事業所の指定日付時点における所属情報をリストで返します。


        Args:
            company_id (int): 事務所ID
            base_date (str): 指定日
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            {
              "employee_group_memberships": [
                {
                  "id": 0,
                  "num": "string",
                  "display_name": "string",
                  "entry_date": "string",
                  "retire_date": "string",
                  "user_id": 0,
                  "login_email": "string",
                  "group_memberships": [
                    {
                      "start_date": "string",
                      "end_date": "string",
                      "group_id": 0,
                      "group_code": "string",
                      "group_name": "string",
                      "level": 0,
                      "position_id": 0,
                      "position_code": "string",
                      "position_name": "string",
                      "parent_group_id": 0,
                      "parent_group_code": "string",
                      "parent_group_name": "string"
                    }
                  ]
                }
              ],
              "total_count": 0
            }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, "employee_group_memberships")
        return self.send_request(request_method, url, payload)


# ===========================================
#     賞与明細(賞与明細の操作)
# ===========================================
    def get_bonuses_employee_payroll_statements(self, **payload):

        """賞与明細一覽の取得

        指定した従業員・日付の扶養親族情報を返します。
        指定した年月に支払いのある賞与明細が返されます。

        Args:
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月
            per (int, optional): 一度に返すアイテム数。上限は100個で、指定なしで先頭から25個のアイテム取得。
            page (int, optional): ページネーションにおけるページ番号であり、指定なしで1番

        Returns:
            dict: like below
            {
              "employee_payroll_statements": [
                {
                  "id": 0,
                  "company_id": 0,
                  "employee_id": 0,
                  "employee_name": "string",
                  "employee_display_name": "string",
                  "employee_num": "string",
                  "closing_date": "string",
                  "pay_date": "string",
                  "fixed": true,
                  "calc_status": "string",
                  "calculated_at": "2019-10-14T06:10:27.766Z",
                  "bonus_amount": "string",
                  "total_allowance_amount": "string",
                  "total_deduction_amount": "string",
                  "net_payment_amount": "string",
                  "gross_payment_amount": "string",
                  "total_taxable_payment_amount": "string",
                  "allowances": [
                    {
                      "name": "string",
                      "amount": "string"
                    }
                  ],
                  "deductions": [
                    {
                      "name": "string",
                      "amount": "string"
                    }
                  ],
                  "remark": "string"
                }
              ],
              "total_count": 0
          }

        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, "bonuses/employee_payroll_statements")
        return self.send_request(request_method, url, payload)

    def get_bonuses_employee_payroll_statement(self, employee_id, **payload):

        """ある従業員の賞与明細を取得

        指定した従業員ID、年月の賞与明細を返します。
        指定した年月に支払いのある賞与明細が返されます。

        Args:
            employee_id (int): 従業員ID
            company_id (int): 事務所ID
            year(int): 対象年
            month(int): 対象月

        Returns:
            dict: like below
            {
              "employee_payroll_statement": {
                "id": 0,
                "company_id": 0,
                "employee_id": 0,
                "employee_name": "string",
                "employee_display_name": "string",
                "employee_num": "string",
                "closing_date": "string",
                "pay_date": "string",
                "fixed": true,
                "calc_status": "string",
                "calculated_at": "2019-10-14T06:20:36.831Z",
                "bonus_amount": "string",
                "total_allowance_amount": "string",
                "total_deduction_amount": "string",
                "net_payment_amount": "string",
                "gross_payment_amount": "string",
                "total_taxable_payment_amount": "string",
                "allowances": [
                  {
                    "name": "string",
                    "amount": "string"
                  }
                ],
                "deductions": [
                  {
                    "name": "string",
                    "amount": "string"
                  }
                ],
                "remark": "string"
              }
        """
        request_method = "get"
        url = urllib.parse.urljoin(self.hr_endpoint, ("/").join(["bonuses/employee_payroll_statements", employee_id]))
        return self.send_request(request_method, url, payload)
