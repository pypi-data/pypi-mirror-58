class Plans():
    def get_terraform_plan(self, plan_id):
        url = self.url + 'plans/{}'.format(plan_id)
        return self._get_handler(url=url)
