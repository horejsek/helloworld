<?php

use Nette\Application\UI\Form,
	Nette\Application as NA;



class ArticlesPresenter extends BasePresenter
{
	/** @var Nette\Database\Table\Selection */
	private $articles;

	protected function startup()
	{
		parent::startup();

		$this->articles = $this->getService('articles');
	}

	public function renderDefault()
	{
		$this->template->articles = $this->articles->order('title');
	}

	public function renderArticle($id)
	{
	    $this->template->article = $this->articles->get($id);
	}
}

